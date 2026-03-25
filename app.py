from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, abort
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'architecture_reactivity_spice_2026_geniel')

# --- "BASE DE DONNÉES" DES PROJETS (DICTIONNAIRE) ---
# C'est ici que tu stockeras les descriptions longues et les ID vidéo
projets_db = {
    'pdc-builder': {
        'titre': 'MS-GA PDC Builder',
        'cate': 'Data Engineering / GovTech / M&E',
        'resume': 'Moteur ETL automatisé et plateforme d\'analyse stratégique pour l\'évaluation des Plans de Développement Communaux (PDC).',
        'description_complete': """
            <h3>Le Défi Institutionnel</h3>
            <p>L'analyse et la consolidation des Plans de Développement Communaux (PDC) pour les partenaires institutionnels impliquaient le traitement manuel de matrices Excel tentaculaires. Ce processus chronophage rendait difficile l'évaluation de la cohérence entre les budgets prévisionnels (se chiffrant en milliards de FCFA) et le cadre logique (Indicateurs, SWOT, Objectifs stratégiques).</p>
            
            <h3>La Solution Architecturale</h3>
            <p>J'ai conçu une architecture <strong>GovTech</strong> complète en Python/Flask, couplée à une base de données PostgreSQL hautement relationnelle. Le cœur du système est un pipeline <strong>ETL (Extract, Transform, Load)</strong> propulsé par Pandas, capable d'ingérer, de nettoyer et de structurer automatiquement les données des fichiers Excel institutionnels.</p>
            
            <h3>Impact & Ingénierie Technique</h3>
            <ul class='list-disc list-inside space-y-2 ml-4'>
                <li><strong>Ingénierie Data (ETL) :</strong> Automatisation de l'ingestion de données massives (Programmes, Projets, Budgets sur 5 ans) via des scripts Python/Pandas, garantissant zéro perte de données et l'intégrité référentielle.</li>
                <li><strong>Digitalisation du Suivi-Évaluation (M&E) :</strong> Modélisation informatique stricte des Cadres Logiques : suivi des Axes Stratégiques, des Matrices SWOT, de l'Arbre à Problèmes, et des Indicateurs de Performance (valeurs de référence et cibles).</li>
                <li><strong>Business Intelligence & Cartographie :</strong> Développement de tableaux de bord interactifs (Chart.js) pour le suivi des KPI financiers, couplés à un <strong>Système d'Information Géographique (SIG)</strong> via Folium/Leaflet pour la cartographie des investissements communaux.</li>
                <li><strong>Génération de Livrables :</strong> Automatisation de l'édition des rapports officiels en un clic, avec génération dynamique de documents Word (<code>python-docx</code>) et PDF (<code>WeasyPrint</code>) directement depuis la base de données.</li>
                <li><strong>Sécurité & RBAC :</strong> Sécurisation des accès par rôles (Administrateur, Directeur, Expert, Agent) avec des vues et permissions strictement isolées sur le back-office.</li>
            </ul>
        """,
        'drive_id': '1MLz5Udo1Q79NX9MzxQwhf8534T_72lkG', # Mets ton ID vidéo Drive ici
        'image_cover': 'pdc_cover.jpg', # Capture d'écran à mettre dans static/img/
        'tags': ['Python (Pandas)', 'ETL', 'PostgreSQL', 'M&E Frameworks', 'Cartographie (SIG)'],
        'color': 'blue'
    },
    'elshaddai-erp': {
        'titre': 'EL-SHADDAÏ SIS & ERP',
        'cate': 'ERP / EdTech / M&E',
        'resume': 'Système d\'Information Scolaire (SIS) complet : gouvernance financière, suivi pédagogique et pilotage stratégique (KPI).',
        'description_complete': """
            <h3>Le Défi Institutionnel</h3>
            <p>En tant que Directeur Adjoint, j'ai constaté que la gestion fragmentée (fichiers Excel multiples) générait des pertes de données, des erreurs de facturation et un manque de visibilité globale. Le besoin était de centraliser la gouvernance administrative, financière et académique dans un outil unique, fiable et capable de générer des indicateurs d'aide à la décision en temps réel.</p>
            
            <h3>La Solution Architecturale</h3>
            <p>J'ai architecturé et développé un ERP institutionnel sur-mesure avec <strong>Python, Flask et SQLAlchemy</strong>. Ce système repose sur un modèle de base de données relationnelle complexe (plus de 15 entités) et intègre une gestion stricte des droits d'accès (RBAC) divisée en 6 portails autonomes (Direction, Comptabilité, Secrétariat, Enseignants, Parents, Admin).</p>
            
            <h3>Impact & Ingénierie Technique</h3>
            <ul class='list-disc list-inside space-y-2 ml-4'>
                <li><strong>Pilotage M&E (Suivi-Évaluation) :</strong> Développement d'un tableau de bord stratégique calculant les KPI institutionnels (taux de recouvrement, parité, zones de risque académique) et intégrant un algorithme prédictif de projection financière sur 5 ans.</li>
                <li><strong>Gouvernance Financière :</strong> Suivi automatisé des flux de trésorerie, gestion des arriérés, et système de notification avec envoi instantané de <strong>reçus numériques cryptés via WhatsApp</strong>.</li>
                <li><strong>Ingénierie Pédagogique :</strong> Algorithme de calcul automatique des moyennes, classements dynamiques (rangs) et génération en un clic des bulletins mensuels et certificats de scolarité.</li>
                <li><strong>Business Intelligence :</strong> Création d'un connecteur d'API JSON RESTful (<code>/api/powerbi</code>) dédié à l'ingestion des données relationnelles en direct par <strong>Microsoft Power BI</strong>.</li>
            </ul>
        """,
        'drive_id': '1Y5uw2xybOzz5mqGA9JI0FDz2RhF2WLiT', # Mets ton ID vidéo Drive ici
        'image_cover': 'elshaddai_cover.jpg', # Capture d'écran à mettre dans static/img/
        'tags': ['Flask', 'RBAC', 'M&E Dashboards', 'API Power BI', 'SQLAlchemy'],
        'color': 'green'
    },
    'msga-learning': {
        'titre': 'MS-GA Learning & CRM',
        'cate': 'SaaS / LMS / FinTech',
        'resume': 'Plateforme d\'e-learning complète intégrant tunnel de vente, paiements automatisés (FedaPay) et génération dynamique de certificats.',
        'description_complete': """
            <h3>Le Défi</h3>
            <p>Le cabinet MS-GA Consulting souhaitait digitaliser la vente de ses séminaires et services d'expertise. Il fallait non seulement un site vitrine, mais surtout un <strong>Espace Client sécurisé</strong> capable de gérer de bout-en-bout le parcours d'un apprenant : de la capture du prospect jusqu'à l'examen final et la certification.</p>
            
            <h3>La Solution Architecturale</h3>
            <p>Conception et développement d'une architecture Full-Stack en <strong>Python/Flask</strong>. Le système est scindé en trois environnements étanches : un site public optimisé pour la conversion (EmailJS), un Espace Apprenant asynchrone (JS/Fetch API), et un Back-Office (Flask-Admin) agissant comme un véritable CRM pour la direction.</p>
            
            <h3>Impact & Ingénierie Technique</h3>
            <ul class='list-disc list-inside space-y-2 ml-4'>
                <li><strong>Tunnel de Vente & CRM :</strong> Suivi automatisé des prospects (Leads) et gestion fine des statuts de commande (En attente, Autorisé, Payé).</li>
                <li><strong>Intégration FinTech :</strong> Connexion à l'API <strong>FedaPay</strong> via JavaScript pour valider les paiements en temps réel et débloquer automatiquement les modules de cours.</li>
                <li><strong>Moteur d'Examen (LMS) :</strong> Conception d'un système de Quiz asynchrone avec calcul algorithmique des scores de validation (Seuil de réussite fixé à 80/100).</li>
                <li><strong>Génération PDF "Pixel Perfect" :</strong> Utilisation avancée de la librairie <strong>ReportLab (Canvas)</strong> pour dessiner mathématiquement, à la volée, des attestations de réussite infalsifiables intégrant les données du client.</li>
            </ul>
        """,
        'drive_id': '1DJOm8d1pvXFDUNZU14B6mpeWx_N40Jip', # Mets ton ID vidéo Drive ici
        'image_cover': 'msga_cms.jpg', 
        'tags': ['Flask', 'ReportLab (PDF)', 'FedaPay API', 'LMS', 'JavaScript (Fetch)'],
        'color': 'purple'
    }
}

# --- ROUTES ---
@app.route('/')
def index():
    # On passe le dictionnaire des projets au template pour l'afficher sur l'accueil
    return render_template('index.html', projets=projets_db)

@app.route('/projet/<projet_id>')
def projet_detail(projet_id):
    # Route dynamique pour afficher le détail d'un projet
    projet = projets_db.get(projet_id)
    if not projet:
        abort(404) # Projet non trouvé
    return render_template('projet_detail.html', projet=projet)

@app.route('/telecharger-cv')
def telecharger_cv():
    # Route pour télécharger le CV PDF
    directory = os.path.join(app.root_path, 'static', 'docs')
    filename = 'Resume_Geniel_GANDAHO.pdf' # Renomme ton PDF ainsi
    return send_from_directory(directory, filename, as_attachment=True)

@app.route('/cv')
def afficher_cv():
    # Affiche la page web du CV interactif
    return render_template('cv.html')

@app.route('/contact', methods=['POST'])
def contact():
    # Logique de simulation d'envoi de formulaire
    nom = request.form.get('nom')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if nom and email and message:
        flash(f"Merci {nom} ! Votre message a bien été envoyé. Je vous recontacte très vite.", "success")
    else:
        flash("Veuillez remplir tous les champs du formulaire.", "error")
        
    return redirect(url_for('index', _anchor='contact'))

if __name__ == '__main__':
    app.run(debug=True)