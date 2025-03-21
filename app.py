# MegaPersonal - Aplicativo de Gerenciamento para Personal Trainers
# Estrutura principal usando Flask para backend e SQLite para banco de dados

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash



app = Flask(__name__)
app.config['SECRET_KEY'] = 'megapersonal_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///megapersonal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Configuração para upload de arquivos
UPLOAD_FOLDER = 'static/uploads/assessments'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crie a pasta de uploads se não existir
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Função para verificar extensões de arquivo permitidas
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Modelos do banco de dados
class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    clients = db.relationship('Client', backref='trainer', lazy=True)
    
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    goal = db.Column(db.String(200))
    health_notes = db.Column(db.Text)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=False)
    workouts = db.relationship('Workout', backref='client', lazy=True)
    assessments = db.relationship('Assessment', backref='client', lazy=True)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    muscle_group = db.Column(db.String(50))
    video_url = db.Column(db.String(200))
    workout_exercises = db.relationship('WorkoutExercise', backref='exercise', lazy=True)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    exercises = db.relationship('WorkoutExercise', backref='workout', lazy=True)

class WorkoutExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    sets = db.Column(db.Integer)
    reps = db.Column(db.String(50))  # Pode ser "12, 10, 8" para pirâmide
    rest_time = db.Column(db.Integer)  # Em segundos
    notes = db.Column(db.Text)
    order = db.Column(db.Integer)  # Ordem do exercício no treino

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    weight = db.Column(db.Float)
    body_fat = db.Column(db.Float)
    chest = db.Column(db.Float)
    waist = db.Column(db.Float)
    hips = db.Column(db.Float)
    arms = db.Column(db.Float)
    thighs = db.Column(db.Float)
    notes = db.Column(db.Text)
    # Novos campos para fotos
    front_photo = db.Column(db.String(255))
    side_photo = db.Column(db.String(255))
    back_photo = db.Column(db.String(255))
    
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20))  # "presente", "ausente", "justificado"
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    notes = db.Column(db.Text)

# Adicione este modelo ao seu arquivo app.py

class ClientUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

# Rotas para API e renderização de páginas
@app.route('/')
def home():
    if 'trainer_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

# Substitua a rota de login existente por esta versão unificada

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Verificar se já está logado como personal ou aluno
    if 'trainer_id' in session:
        return redirect(url_for('dashboard'))
    if 'client_id' in session:
        return redirect(url_for('client_dashboard'))
    
    error = None
    user_type = request.form.get('user_type', 'trainer')  # Valor padrão é trainer
    
    if request.method == 'POST':
        user_type = request.form.get('user_type')
        
        if user_type == 'trainer':
            # Login de personal trainer
            email = request.form.get('email')
            password = request.form.get('password')
            
            trainer = Trainer.query.filter_by(email=email).first()
            
            if trainer and check_password_hash(trainer.password, password):
                session['trainer_id'] = trainer.id
                session['trainer_name'] = trainer.name
                return redirect(url_for('dashboard'))
            else:
                error = 'Email ou senha incorretos'
        
        elif user_type == 'student':
            # Login de aluno
            username = request.form.get('username')
            password = request.form.get('password')
            
            client_user = ClientUser.query.filter_by(username=username).first()
            
            if client_user and check_password_hash(client_user.password, password):
                session['client_id'] = client_user.client_id
                client_user.last_login = datetime.utcnow()
                db.session.commit()
                return redirect(url_for('client_dashboard'))
            else:
                error = 'Nome de usuário ou senha incorretos'
    
    return render_template('login.html', error=error, user_type=user_type)

# Adicione esta rota para garantir que o logout funcione independente do tipo de usuário
@app.route('/logout')
def logout():
    session.pop('trainer_id', None)
    session.pop('trainer_name', None)
    session.pop('client_id', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    trainer = Trainer.query.get(session['trainer_id'])
    clients = Client.query.filter_by(trainer_id=trainer.id).all()
    
    # Contagem de clientes, treinos, etc.
    client_count = len(clients)
    today = datetime.utcnow().date()
    
    # Sessões agendadas para hoje
    attendances_today = Attendance.query.filter(
        Attendance.client_id.in_([client.id for client in clients]),
        db.func.date(Attendance.date) == today
    ).all()
    
    return render_template('dashboard.html', 
                          trainer=trainer, 
                          clients=clients, 
                          client_count=client_count,
                          attendances_today=attendances_today)

@app.route('/clients')
def client_list():
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    trainer = Trainer.query.get(session['trainer_id'])
    clients = Client.query.filter_by(trainer_id=trainer.id).all()
    
    return render_template('clients.html', trainer=trainer, clients=clients)

@app.route('/client/<int:client_id>')
def client_detail(client_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    client = Client.query.get_or_404(client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    workouts = Workout.query.filter_by(client_id=client.id).all()
    assessments = Assessment.query.filter_by(client_id=client.id).order_by(Assessment.date.desc()).all()
    
    return render_template('client_detail.html', 
                          client=client, 
                          workouts=workouts, 
                          assessments=assessments)

@app.route('/client/new', methods=['GET', 'POST'])
def client_new():
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')
        height = request.form.get('height')
        weight = request.form.get('weight')
        goal = request.form.get('goal')
        health_notes = request.form.get('health_notes')
        
        client = Client(
            name=name,
            email=email,
            phone=phone,
            age=age,
            height=height,
            weight=weight,
            goal=goal,
            health_notes=health_notes,
            trainer_id=session['trainer_id']
        )
        
        db.session.add(client)
        db.session.commit()
        
        return redirect(url_for('client_detail', client_id=client.id))
    
    return render_template('client_form.html')

@app.route('/workout/new/<int:client_id>', methods=['GET', 'POST'])
def workout_new(client_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    client = Client.query.get_or_404(client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        
        workout = Workout(
            name=name,
            description=description,
            client_id=client.id
        )
        
        db.session.add(workout)
        db.session.commit()
        
        return redirect(url_for('workout_edit', workout_id=workout.id))
    
    return render_template('workout_form.html', client=client)

@app.route('/workout/edit/<int:workout_id>', methods=['GET', 'POST'])
def workout_edit(workout_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    workout = Workout.query.get_or_404(workout_id)
    client = Client.query.get(workout.client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    # Obter todos os exercícios disponíveis
    exercises = Exercise.query.all()
    
    # Obter exercícios já adicionados ao treino
    workout_exercises = WorkoutExercise.query.filter_by(workout_id=workout.id).order_by(WorkoutExercise.order).all()
    
    if request.method == 'POST':
        # Verificar se é ação de adicionar exercício
        exercise_id = request.form.get('exercise_id')
        
        if exercise_id:
            exercise_id = int(exercise_id)
            sets = int(request.form.get('sets', 3))
            reps = request.form.get('reps', '12')
            rest_time = int(request.form.get('rest_time', 60))
            notes = request.form.get('notes', '')
            order = int(request.form.get('order', len(workout_exercises) + 1))
            
            # Verificar se o exercício existe
            exercise = Exercise.query.get(exercise_id)
            if not exercise:
                flash('Exercício não encontrado.', 'error')
                return redirect(url_for('workout_edit', workout_id=workout.id))
            
            # Criar novo exercício de treino
            workout_exercise = WorkoutExercise(
                workout_id=workout.id,
                exercise_id=exercise_id,
                sets=sets,
                reps=reps,
                rest_time=rest_time,
                notes=notes,
                order=order
            )
            
            # Adicionar ao banco de dados
            db.session.add(workout_exercise)
            db.session.commit()
            
            flash('Exercício adicionado com sucesso!', 'success')
            return redirect(url_for('workout_edit', workout_id=workout.id))
        
        # Verificar se é ação de remover exercício
        remove_id = request.form.get('remove_exercise_id')
        if remove_id:
            workout_exercise = WorkoutExercise.query.get(int(remove_id))
            if workout_exercise and workout_exercise.workout_id == workout.id:
                db.session.delete(workout_exercise)
                db.session.commit()
                flash('Exercício removido com sucesso!', 'success')
            return redirect(url_for('workout_edit', workout_id=workout.id))
    
    return render_template('workout_edit.html', 
                          workout=workout, 
                          client=client, 
                          exercises=exercises,
                          workout_exercises=workout_exercises)

@app.route('/assessment/new/<int:client_id>', methods=['GET', 'POST'])
def assessment_new(client_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    client = Client.query.get_or_404(client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    if request.method == 'POST':
        weight = request.form.get('weight')
        body_fat = request.form.get('body_fat')
        chest = request.form.get('chest')
        waist = request.form.get('waist')
        hips = request.form.get('hips')
        arms = request.form.get('arms')
        thighs = request.form.get('thighs')
        notes = request.form.get('notes')
        
        # Criar nova avaliação
        assessment = Assessment(
            client_id=client.id,
            weight=weight,
            body_fat=body_fat,
            chest=chest,
            waist=waist,
            hips=hips,
            arms=arms,
            thighs=thighs,
            notes=notes
        )
        
        # Processar uploads de fotos
        # Foto frontal
        if 'front_photo' in request.files and request.files['front_photo'].filename:
            front_photo = request.files['front_photo']
            if allowed_file(front_photo.filename):
                # Criar nome de arquivo seguro usando ID do cliente e timestamp
                filename = f"client_{client.id}_front_{int(datetime.utcnow().timestamp())}"
                extension = front_photo.filename.rsplit('.', 1)[1].lower()
                filename = f"{filename}.{extension}"
                
                # Salvar o arquivo
                front_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                assessment.front_photo = filename
        
        # Foto lateral
        if 'side_photo' in request.files and request.files['side_photo'].filename:
            side_photo = request.files['side_photo']
            if allowed_file(side_photo.filename):
                # Criar nome de arquivo seguro
                filename = f"client_{client.id}_side_{int(datetime.utcnow().timestamp())}"
                extension = side_photo.filename.rsplit('.', 1)[1].lower()
                filename = f"{filename}.{extension}"
                
                # Salvar o arquivo
                side_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                assessment.side_photo = filename
        
        # Foto posterior
        if 'back_photo' in request.files and request.files['back_photo'].filename:
            back_photo = request.files['back_photo']
            if allowed_file(back_photo.filename):
                # Criar nome de arquivo seguro
                filename = f"client_{client.id}_back_{int(datetime.utcnow().timestamp())}"
                extension = back_photo.filename.rsplit('.', 1)[1].lower()
                filename = f"{filename}.{extension}"
                
                # Salvar o arquivo
                back_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                assessment.back_photo = filename
        
        # Salvar a avaliação no banco de dados
        db.session.add(assessment)
        db.session.commit()
        
        # Atualizar o peso do cliente
        client.weight = weight
        db.session.commit()
        
        return redirect(url_for('client_detail', client_id=client.id))
    
    # Passando a data atual para o template
    now = datetime.utcnow()
    
    return render_template('assessment_form.html', client=client, now=now)

# API Endpoints para aplicativo móvel
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    trainer = Trainer.query.filter_by(email=email).first()
    
    if trainer and check_password_hash(trainer.password, password):
        return jsonify({
            'success': True,
            'trainer_id': trainer.id,
            'name': trainer.name
        })
    
    return jsonify({
        'success': False,
        'message': 'Credenciais inválidas'
    })

@app.route('/api/clients/<int:trainer_id>')
def api_clients(trainer_id):
    clients = Client.query.filter_by(trainer_id=trainer_id).all()
    
    client_list = []
    for client in clients:
        client_list.append({
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'phone': client.phone,
            'goal': client.goal
        })
    
    return jsonify(client_list)

@app.route('/api/workouts/<int:client_id>')
def api_workouts(client_id):
    workouts = Workout.query.filter_by(client_id=client_id).all()
    
    workout_list = []
    for workout in workouts:
        workout_exercises = WorkoutExercise.query.filter_by(workout_id=workout.id).order_by(WorkoutExercise.order).all()
        
        exercises = []
        for we in workout_exercises:
            exercise = Exercise.query.get(we.exercise_id)
            exercises.append({
                'id': exercise.id,
                'name': exercise.name,
                'sets': we.sets,
                'reps': we.reps,
                'rest_time': we.rest_time,
                'notes': we.notes
            })
        
        workout_list.append({
            'id': workout.id,
            'name': workout.name,
            'description': workout.description,
            'exercises': exercises
        })
    
    return jsonify(workout_list)

# Adicione estas rotas ao seu arquivo app.py

@app.route('/exercises')
def exercises():
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    exercises = Exercise.query.all()
    return render_template('exercises.html', exercises=exercises)

@app.route('/exercise/new', methods=['POST'])
def exercise_new():
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        muscle_group = request.form.get('muscle_group')
        
        # Determinar qual URL de mídia usar com base no tipo selecionado
        media_type = request.form.get('media_type')
        if media_type == 'youtube':
            video_url = request.form.get('video_url')
        elif media_type == 'shorts':
            video_url = request.form.get('shorts_url')
        elif media_type == 'gif':
            video_url = request.form.get('gif_url')
        else:
            video_url = ''
        
        exercise = Exercise(
            name=name,
            description=description,
            muscle_group=muscle_group,
            video_url=video_url
        )
        
        db.session.add(exercise)
        db.session.commit()
        
        return redirect(url_for('exercises'))
    
    return redirect(url_for('exercises'))

@app.route('/exercise/<int:exercise_id>')
def exercise_detail(exercise_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    exercise = Exercise.query.get_or_404(exercise_id)
    return jsonify({
        'id': exercise.id,
        'name': exercise.name,
        'description': exercise.description,
        'muscle_group': exercise.muscle_group,
        'video_url': exercise.video_url
    })

@app.route('/exercise/edit/<int:exercise_id>', methods=['GET', 'POST'])
def exercise_edit(exercise_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    exercise = Exercise.query.get_or_404(exercise_id)
    
    if request.method == 'POST':
        exercise.name = request.form.get('name')
        exercise.description = request.form.get('description')
        exercise.muscle_group = request.form.get('muscle_group')
        
        # Determinar qual URL de mídia usar com base no tipo selecionado
        media_type = request.form.get('media_type')
        if media_type == 'youtube':
            exercise.video_url = request.form.get('video_url')
        elif media_type == 'shorts':
            exercise.video_url = request.form.get('shorts_url')
        elif media_type == 'gif':
            exercise.video_url = request.form.get('gif_url')
        
        db.session.commit()
        return redirect(url_for('exercises'))
    
    return render_template('exercise_edit.html', exercise=exercise)

# Adicione estas rotas ao seu arquivo app.py

@app.route('/client/user/<int:client_id>', methods=['GET', 'POST'])
def client_user_manage(client_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    client = Client.query.get_or_404(client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    # Buscar usuário existente ou criar um novo
    client_user = ClientUser.query.filter_by(client_id=client_id).first()
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Verificar se o username já existe (exceto para o usuário atual)
        existing_user = ClientUser.query.filter_by(username=username).first()
        if existing_user and existing_user.client_id != client_id:
            return render_template('client_user.html', client=client, client_user=client_user, error='Nome de usuário já existe')
        
        if client_user:
            # Atualizar usuário existente
            client_user.username = username
            if password:  # Só atualiza a senha se uma nova for fornecida
                client_user.password = generate_password_hash(password)
        else:
            # Criar novo usuário
            client_user = ClientUser(
                username=username,
                password=generate_password_hash(password),
                client_id=client_id
            )
            db.session.add(client_user)
        
        db.session.commit()
        return redirect(url_for('client_detail', client_id=client_id))
    
    return render_template('client_user.html', client=client, client_user=client_user)

# Rotas para login e acesso do cliente
@app.route('/aluno/login', methods=['GET', 'POST'])
def client_login():
    if 'client_id' in session:
        return redirect(url_for('client_dashboard'))
    
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = ClientUser.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['client_id'] = user.client_id
            user.last_login = datetime.utcnow()
            db.session.commit()
            return redirect(url_for('client_dashboard'))
        else:
            error = 'Nome de usuário ou senha incorretos'
    
    return render_template('client_login.html', error=error)

@app.route('/aluno/logout')
def client_logout():
    return redirect(url_for('logout'))

@app.route('/aluno/dashboard')
def client_dashboard():
    if 'client_id' not in session:
        return redirect(url_for('client_login'))
    
    client = Client.query.get(session['client_id'])
    workouts = Workout.query.filter_by(client_id=client.id).all()
    
    return render_template('client_dashboard.html', client=client, workouts=workouts)

@app.route('/aluno/treino/<int:workout_id>')
def client_workout_view(workout_id):
    if 'client_id' not in session:
        return redirect(url_for('client_login'))
    
    workout = Workout.query.get_or_404(workout_id)
    
    # Verifica se o treino pertence ao cliente logado
    if workout.client_id != session['client_id']:
        return redirect(url_for('client_dashboard'))
    
    workout_exercises = WorkoutExercise.query.filter_by(workout_id=workout.id).order_by(WorkoutExercise.order).all()
    
    return render_template('client_workout_view.html', workout=workout, workout_exercises=workout_exercises)

@app.route('/aluno/exercicio/<int:exercise_id>')
def client_exercise_view(exercise_id):
    if 'client_id' not in session:
        return redirect(url_for('client_login'))
    
    exercise = Exercise.query.get_or_404(exercise_id)
    
    # Buscar exercícios relacionados (mesmo grupo muscular, exceto o atual)
    related_exercises = Exercise.query.filter(
        Exercise.muscle_group == exercise.muscle_group,
        Exercise.id != exercise.id
    ).limit(4).all()
    
    return render_template('client_exercise_view.html', exercise=exercise, related_exercises=related_exercises)

@app.route('/assessment/<int:assessment_id>')
def assessment_view(assessment_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    assessment = Assessment.query.get_or_404(assessment_id)
    client = Client.query.get(assessment.client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    return render_template('assessment_view.html', assessment=assessment, client=client)

@app.route('/client/<int:client_id>/assessments/compare', methods=['GET', 'POST'])
def assessment_compare(client_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    client = Client.query.get_or_404(client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    # Obter todas as avaliações do cliente, ordenadas por data
    assessments = Assessment.query.filter_by(client_id=client.id).order_by(Assessment.date.desc()).all()
    
    before = None
    after = None
    before_id = None
    after_id = None
    
    if request.method == 'POST':
        before_id = request.form.get('before_assessment', type=int)
        after_id = request.form.get('after_assessment', type=int)
        
        if before_id and after_id:
            before = Assessment.query.get(before_id)
            after = Assessment.query.get(after_id)
    
    return render_template('assessment_compare.html', 
                           client=client, 
                           assessments=assessments, 
                           before=before, 
                           after=after, 
                           before_id=before_id, 
                           after_id=after_id)

@app.route('/client/delete/<int:client_id>', methods=['POST'])
def client_delete(client_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    client = Client.query.get_or_404(client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    try:
        # Excluir todas as avaliações e suas fotos
        assessments = Assessment.query.filter_by(client_id=client.id).all()
        for assessment in assessments:
            # Remover arquivos de fotos, se existirem
            if assessment.front_photo:
                try:
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], assessment.front_photo))
                except Exception as e:
                    print(f"Erro ao excluir foto frontal: {e}")
            
            if assessment.side_photo:
                try:
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], assessment.side_photo))
                except Exception as e:
                    print(f"Erro ao excluir foto lateral: {e}")
            
            if assessment.back_photo:
                try:
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], assessment.back_photo))
                except Exception as e:
                    print(f"Erro ao excluir foto posterior: {e}")
            
            db.session.delete(assessment)
        
        # Excluir todos os treinos e exercícios relacionados
        workouts = Workout.query.filter_by(client_id=client.id).all()
        for workout in workouts:
            # Excluir exercícios do treino
            WorkoutExercise.query.filter_by(workout_id=workout.id).delete()
            db.session.delete(workout)
        
        # Excluir registros de presença
        Attendance.query.filter_by(client_id=client.id).delete()
        
        # Excluir credenciais de acesso
        client_user = ClientUser.query.filter_by(client_id=client.id).first()
        if client_user:
            db.session.delete(client_user)
        
        # Por fim, excluir o cliente
        client_name = client.name  # Guarda o nome para usar na mensagem
        db.session.delete(client)
        db.session.commit()
        
        flash(f'Cliente {client_name} excluído com sucesso.', 'success')
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao excluir cliente: {e}")
        flash('Ocorreu um erro ao excluir o cliente.', 'error')
    
    # Redirecionando para a página de clientes
    return redirect(url_for('client_list'))

@app.route('/client/edit/<int:client_id>', methods=['GET', 'POST'])
def client_edit(client_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    client = Client.query.get_or_404(client_id)
    
    # Verificar se o cliente pertence ao trainer logado
    if client.trainer_id != session['trainer_id']:
        return redirect(url_for('clients'))
    
    if request.method == 'POST':
        # Obter os dados do formulário
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age') or None
        height = request.form.get('height') or None
        weight = request.form.get('weight') or None
        goal = request.form.get('goal')
        health_notes = request.form.get('health_notes')
        
        # Validação básica
        if not name or not email or not phone:
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            return render_template('client_edit.html', client=client)
        
        try:
            # Atualizar os dados do cliente
            client.name = name
            client.email = email
            client.phone = phone
            client.age = age
            client.height = height
            client.weight = weight
            client.goal = goal
            client.health_notes = health_notes
            
            # Salvar no banco de dados
            db.session.commit()
            
            # Mensagem de sucesso
            flash('Cliente atualizado com sucesso!', 'success')
            return redirect(url_for('client_detail', client_id=client.id))
            
        except Exception as e:
            # Em caso de erro, desfaz as alterações
            db.session.rollback()
            print(f"Erro ao atualizar cliente: {e}")
            flash('Erro ao atualizar os dados do cliente.', 'error')
    
    # Se for uma requisição GET ou em caso de erro, mostra o formulário
    return render_template('client_edit.html', client=client)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)