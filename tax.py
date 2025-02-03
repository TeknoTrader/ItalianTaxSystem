import streamlit as st
import pandas as pd


def get_dati_categoria(categoria):
    """
    Restituisce un DataFrame con le informazioni per la categoria selezionata
    """
    if categoria == 'Commerciante':
        return pd.DataFrame({
            'Voce': [
                'Spese fisse annue',
                'Aliquote',
                'Agevolazioni',
                'Svantaggi',
                'Vantaggi'
            ],
            'Dettagli': [
                '4500€ (contributi INPS, assicurazioni)',
                '5% sul reddito (regime forfettario)',
                'Tassazione agevolata, contributi ridotti',
                'Responsabilità personale, minore copertura previdenziale',
                'Bassa burocrazia, gestione flessibile'
            ]
        })

    elif categoria == 'Consulente':
        return pd.DataFrame({
            'Voce': [
                'Commercialista',
                'Aliquote',
                'Agevolazioni',
                'Svantaggi',
                'Vantaggi'
            ],
            'Dettagli': [
                '0-200€ (spese amministrative base)',
                '26 + 5% sul reddito',
                'Detrazioni fiscali standard',
                'Tassazione progressiva, maggiori oneri',
                'Stabilità, protezioni sociali standard'
            ]
        })

    elif categoria == 'SRLs':
        return pd.DataFrame({
            'Voce': [
                'Spese fisse annue',
                'Aliquote',
                'Agevolazioni',
                'Svantaggi',
                'Vantaggi'
            ],
            'Dettagli': [
                '1.500-3.000€ (commercialista, revisore, adempimenti)',
                '24% IRES, IRAP variabile',
                'Crediti d\'imposta, incentivi per investimenti',
                'Alta burocrazia, costi di gestione elevati',
                'Responsabilità limitata, credibilità professionale'
            ]
        })


def main():
    # Titolo dell'applicazione
    st.title('Confronto Tipologie')

    # Creazione del sidebar per il toolbox
    with st.sidebar:
        st.header('Seleziona la Categoria')

        # Radio button per la selezione
        categoria = st.radio(
            'Scegli una categoria:',
            ['Commerciante', 'Consulente', 'SRLs']
        )

    # Recupera i dati per la categoria selezionata
    dati = get_dati_categoria(categoria)

    # Mostra la tabella
    st.header(f'Dettagli per {categoria}')
    st.table(dati)


# Esecuzione dell'applicazione
if __name__ == '__main__':
    main()
