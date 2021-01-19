Script permettant de générer de façon automatique et en 1min environ un excel récapitulatif de votre portefeuille crypto.
Il récupère de façon automatique la liste des cryptos que vous détenez sur les échangeurs et leur valeurs.
Comme ça plus besoin de tenir un excel à la main 😉


## Echangeurs pris en compte actuelement:
- Binance
- Coinbase

A terme vous pourrez aussi l'utiliser avec d'autres échangeurs et vous pouvez ajouter toute adresse ethereum.

## Pré-requis
- Python ([installer Python](https://www.python.org/downloads/))
- pip

## Installation
- Téléchargez le zip de ce projet
- Déziper le dosier
- Ouvrir un terminal et se rendre jusqu'au dossier avec la commande *cd*
- faire un *pip install -r requirements.txt* pour installer toutes les dépendances
- modifier le fichier config.py

## Créer des API Key / API Secret
- Créer une [clef API Binance](https://www.binance.com/fr/support/faq/360002502072)
- Créer une [clef API Coinbase](https://help.coinbase.com/en/pro/other-topics/api/how-do-i-create-an-api-key-for-coinbase-pro)

## Utilisation
  python -m main
  
