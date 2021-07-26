<p  align="center">
<h1  align="center">Taille-qui-compte</h3>
</p>

## Sommaire

*  [Contexte du projet](#contexte-du-projet)

*  [Commencer](#commencer)

*  [Utilisation](#utilisation)

*  [Auteurs](#auteurs)


## Contexte du projet

La société "Little Sister" souhaite développer un nouveau type de caméras de surveillance pour l'espace publique.

Elle souhaite mettre en avant une fonctionnalité de reconnaissance d'éléments sur une image afin de pouvoir identifier des cas, des situations qui peuvent survenir dans la vie de tous les jours.

Elle possède un modèle que vous lui avez fourni précédemment, qui permet de détecter des éléments qu'on peut retrouver sur une image. Première étape vers leur objectif final : prévenir des situations pouvant être dangereuses, voir des incivilités.

La performance de ce modèle ne répond aujourd'hui pas aux espérances de la société. Il faut donc tout d'abord **analyser la performance d'un modèle sans préprocessing** et essayer d'améliorer la qualité du modèle avec du préprocessing (ici data augmentation).

## Commencer

Pour avoir une copie locale et lancer le programme, suivez ces étapes.

### Installation

1. Cloner le répertoire
```git
git clone https://github.com/Nicolas-Malgat/Taille-qui-compte.git
```
2. Créer un environnement conda avec
```bash
conda create --name <env> --file environment.txt
```
## Utilisation

- Lancer [jup_entrainement_modele.ipynb](https://github.com/Nicolas-Malgat/Taille-qui-compte/blob/main/jup_entrainement_modele.ipynb "jup_entrainement_modele.ipynb")
    - Telechargement des donnees
    - Extration des donnees
	- Entrainement et generation des modèles ( [model.h5](https://github.com/Nicolas-Malgat/Taille-qui-compte/blob/main/model.h5 "model.h5") et [augmented_model.h5.h5](https://github.com/Nicolas-Malgat/Taille-qui-compte/blob/main/augmented_model.h5.h5 "augmented_model.h5.h5") ) pour les comparer et observer l'influence de la data augmentation

#### _optionnel_
___
- Lancer [jup_augmentation_donnees.ipynb](https://github.com/Nicolas-Malgat/Taille-qui-compte/blob/main/jup_augmentation_donnees.ipynb)
	- Ce notebook charge une image et montre les modifications apportees par la data augmentation
___
## Auteur

Nicolas Malgat
