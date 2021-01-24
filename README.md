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
- Dézipez le dosier
- Ouvrir un terminal et se rendre jusqu'au dossier avec la commande *cd*
- faire un *pip install -r requirements.txt* pour installer toutes les dépendances
- modifiez le fichier .env pour:
  - y ajouter vos clés API.
  - modifier la constante using_Binance ( respectivement using_Coinbase) avec la valeur "True" si vous souhaitez utiliser le service Binance (resp. Coinbase) et "False" dans le cas contraire.


## Créer des API Key / API Secret

- Pour créer une clef API Binance vous pouvez suivre [ce tutoriel de Binance en français](https://www.binance.com/fr/support/faq/360002502072)
  - Cochez uniquement "Permettre la lecture"
  
- Pour créer une clé API Coinbase il faut:
  - se rendre sur https://developers.coinbase.com/ -> My Apps -> Nouvelle Clé API
  
    -Dans la section compte sélectionnez toutes les cryptos monnaies que vous souhaitez suivre
    
    -🔐 Cochez uniquement dans API v2 permission la case "wallet:account:read" (pas besoin du reste)

## Utilisation
Après le procesus d'intallation et notament la modification du fichier de config.py comme décrit plus haut.
Il vous suffit de lancer la commande suivante pour généré votre rapport.

    python -m main
  
