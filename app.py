from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, abort
import os
from dotenv import load_dotenv

# Charge les variables cachées du fichier .env (en local)
load_dotenv()

app = Flask(__name__)
# On récupère la clé. S'il ne la trouve pas (ex: oubli), on met une clé bidon 'dev_key' qui ne craint rien en public.
app.secret_key = os.environ.get('SECRET_KEY', 'cle_de_developpement@123')

# ... la suite de ton code avec projets_db ...
# --- "BASE DE DONNÉES" DES PROJETS (DICTIONNAIRE) ---
# C'est ici que tu stockeras les descriptions longues et les ID vidéo
projets_db = {
    'pdc-builder': {
        'titre': 'MS-GA PDC Builder',
        'cate': 'Data & Suivi-Évaluation',
        'resume': "Plateforme de digitalisation et d'analyse des Plans de Développement Communaux (PDC).",
        'description_complete': """
            <h3>Le Défi Institutionnel</h3>
            <p>L'analyse des Plans de Développement Communaux (PDC) reposait principalement sur des fichiers Excel volumineux et difficiles à exploiter. Ce mode de gestion rendait complexe le suivi des budgets, des indicateurs et la cohérence globale des données pour les décideurs.</p>
            
            <h3>La Solution Architecturale</h3>
            <p>J'ai conçu une application web en Python (Flask) couplée à une base de données relationnelle (PostgreSQL) permettant de centraliser, structurer et exploiter les données des PDC de manière sécurisée.</p>
            
            <h3>Résultats & Apports Techniques</h3>
            <ul class='list-disc list-inside space-y-2 ml-4'>
                <li><strong>Automatisation des données :</strong> Import, nettoyage et structuration des données (projets, budgets, indicateurs) directement à partir de fichiers Excel.</li>
                <li><strong>Structuration du M&E :</strong> Intégration stricte des cadres logiques (axes stratégiques, indicateurs, matrices SWOT).</li>
                <li><strong>Tableaux de bord :</strong> Visualisation claire des données financières et des indicateurs de performance clés.</li>
                <li><strong>Cartographie :</strong> Visualisation des investissements par localité.</li>
                <li><strong>Génération de rapports :</strong> Export automatique des synthèses en formats Word et PDF.</li>
                <li><strong>Gestion des accès :</strong> Système de rôles (RBAC) pour sécuriser l'accès aux données selon les profils utilisateurs.</li>
            </ul>
        """,
        'drive_id': '1MLz5Udo1Q79NX9MzxQwhf8534T_72lkG', 
        'image_cover': 'pdc_cover.jpg', 
        'tags': ['Python (Flask)', 'PostgreSQL', 'M&E Frameworks', 'Cartographie', 'Automatisation Excel'],
        'color': 'blue'
    },
    
    'elshaddai-erp': {
        'titre': 'EL-SHADDAÏ SIS & ERP',
        'cate': 'Gestion Scolaire & M&E',
        'resume': "Système centralisé pour la gestion administrative, financière et le suivi pédagogique de l'établissement.",
        'description_complete': """
            <h3>Le Défi</h3>
            <p>La gestion fragmentée sur de multiples fichiers Excel générait des erreurs de facturation, des pertes de temps administratif et un manque de visibilité globale sur la santé financière et académique de l'école. Le besoin était de centraliser l'information pour faciliter la prise de décision.</p>
            
            <h3>La Solution Architecturale</h3>
            <p>J'ai développé une application web sur-mesure (Python/Flask) adossée à une base de données structurée couvrant les principaux processus de l'école. Le système propose des portails dédiés selon les rôles (Direction, Comptabilité, Secrétariat, Enseignants).</p>
            
            <h3>Résultats & Apports Techniques</h3>
            <ul class='list-disc list-inside space-y-2 ml-4'>
                <li><strong>Gouvernance Financière :</strong> Suivi centralisé de la trésorerie, gestion des arriérés, et système de reçus numériques envoyés via WhatsApp.</li>
                <li><strong>Suivi Pédagogique :</strong> Calcul automatique des moyennes, classements et génération des bulletins scolaires.</li>
                <li><strong>Tableaux de bord M&E :</strong> Outil de projection financière et suivi des indicateurs de recouvrement en temps réel.</li>
                <li><strong>Connectivité Data :</strong> Interfaçage sécurisé avec Microsoft Power BI pour l'analyse décisionnelle de la direction.</li>
            </ul>
        """,
        'drive_id': '1Y5uw2xybOzz5mqGA9JI0FDz2RhF2WLiT',
        'image_cover': 'elshaddai_cover.jpg', 
        'tags': ['Flask', 'Microsoft Power BI', 'Gestion Financière', 'Automatisation', 'Base de données'],
        'color': 'green'
    },
    
    'msga-learning': {
        'titre': 'MS-GA Learning & CRM',
        'cate': 'E-learning & Digitalisation',
        'resume': "Plateforme de formation en ligne avec gestion des inscriptions, paiements automatisés et certifications.",
        'description_complete': """
            <h3>Le Défi</h3>
            <p>Le cabinet souhaitait digitaliser la vente de ses séminaires et automatiser le parcours de l'apprenant : de la prospection initiale jusqu'à la validation des acquis et la délivrance de l'attestation, le tout sans intervention manuelle lourde.</p>
            
            <h3>La Solution Architecturale</h3>
            <p>Conception d'une plateforme web complète comprenant un site vitrine pour la conversion, un Espace Apprenant sécurisé, et un tableau de bord administratif (CRM) pour le suivi des cohortes par la direction.</p>
            
            <h3>Résultats & Apports Techniques</h3>
            <ul class='list-disc list-inside space-y-2 ml-4'>
                <li><strong>Gestion des apprenants (CRM) :</strong> Suivi centralisé des inscriptions, des prospects et des statuts d'avancement.</li>
                <li><strong>Paiements en ligne :</strong> Intégration de l'API FedaPay pour valider les paiements et débloquer automatiquement les modules de cours.</li>
                <li><strong>Évaluations :</strong> Système de quiz intégrés avec calcul des scores et seuils de validation.</li>
                <li><strong>Certifications :</strong> Génération automatisée d'attestations PDF personnalisées dès la réussite du module.</li>
            </ul>
        """,
        'drive_id': '1DJOm8d1pvXFDUNZU14B6mpeWx_N40Jip', 
        'image_cover': 'msga_cms.jpg',  
        'tags': ['Web App', 'FedaPay API', 'CRM', 'LMS', 'Génération PDF'],
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