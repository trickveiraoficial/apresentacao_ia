import streamlit as st

st.set_page_config(page_title="Apresentação Profissional", layout="centered")

st.markdown(
    """
    <style>
    /* Importando a fonte Roboto do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    /* Importando Font Awesome para ícones */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');

    /* Remove os elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Remove padding e margens do container principal do Streamlit */
    .block-container {
        padding: 0 !important;
        margin: 0 auto;
        max-width: 100%;
        overflow: hidden;
    }

    /* Estilização geral da página */
    html, body {
        margin: 0;
        padding: 0;
        overflow: hidden;
        background: linear-gradient(135deg, #1e1e1e, #2b2b2b);
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        height: 100vh;
    }

    /* Container centralizado */
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        padding: 20px;
    }

    /* Título */
    .title {
        font-size: 2.5rem;
        margin-bottom: 20px;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    /* Container do vídeo */
    .video-container {
        width: 100%;
        max-width: 800px;
        aspect-ratio: 16 / 9;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }

    iframe {
        width: 100%;
        height: 100%;
        border: none;
        border-radius: 10px;
    }

    /* Botão do LinkedIn */
    .linkedin-button {
        margin-top: 20px;
        padding: 12px 24px;
        background-color: #0077B5; /* Cor oficial do LinkedIn */
        color: white;
        border-radius: 5px;
        opacity: 1; /* Garante que o botão não esteja esmaecido */
        text-decoration: none;
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .linkedin-button:hover {
        background-color: #005582; /* Tom mais escuro ao passar o mouse */
        transform: translateY(-2px); /* Leve elevação */
    }

    .linkedin-button i {
        font-size: 1.5rem; /* Tamanho do ícone */
    }

    /* Responsividade */
    @media (max-width: 600px) {
        .title {
            font-size: 1.8rem;
        }
        .video-container {
            max-width: 100%;
        }
        .linkedin-button {
            font-size: 1rem;
            padding: 10px 20px;
        }
    }
    </style>

    <div class="container">
        <div class="title">Vídeo de Apresentação Gerado por IA</div>
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/Vspvgu7q5qc?controls=1&modestbranding=1&rel=0&fs=0&iv_load_policy=3" 
                    title="Vídeo de apresentação gerado por IA" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
            </iframe>
        </div>
        <a href="https://www.linkedin.com/in/ids-oliveira/" target="_blank" class="linkedin-button" aria-label="Visitar perfil no LinkedIn">
            <i class="fab fa-linkedin"></i>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)