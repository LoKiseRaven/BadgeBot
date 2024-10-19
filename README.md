# Discord Bot Active Developer Badge 

- **[English version 🇺🇸](#english-version-🇺🇸)**
- **[Version française 🇫🇷](#version-française-🇫🇷)**

# English version 🇺🇸

## Requirements

### Python

First, you need to have Python installed, version 3 or higher. If you don't have it, simply install it through [Python installation page](https://www.python.org/downloads/)


### Discord.py
Then install discord.py which is required for running your bot :

```
pip install discord-py
```

## Creating a bot 

1) First go to [Discord Developer Portal](https://discord.com/developers/applications)
2) Then click on "New application" on the top right corner, and give it a name (the name doesn't really matter)
3)  Go to OAuth2
4) Check `bot` and `applications.commands`
5) Scroll to `BOT PERMISSIONS`
6) Check `Administrator`
7) Copy the generated URL and paste it on your browser
8) Add the bot to your server. RECOMMENDED : you can create a new server for it, and make it a Community server (which will be required to claim the badge)
9) Go back to Discord Developer Portal, and go to `Bot`
10) Uncheck `PUBLIC BOT` and check all Intents (`PRESENCE INTENT`, `SERVER MEMBERS INTENT` `MESSAGE CONTENT INTENT`)
![intents to check](screens/intents.png)
11) Press `Reset Token` button and copy your bot token (⚠️ do **NOT** share it with anyone)
12) Finally go to `bot.py` file and paste it inside the parenthesis of `bot.run("YOUR TOKEN")`

### Claim badge
After using the /hello command, you'll have to wait at least 24 hours to be able to claim your badge at [Active Developer Badge](https://discord.com/developers/active-developer).

> [!IMPORTANT]
> The /hello command may not be available immediately after starting the bot. It could take up to an hour to become accessible.


---


# Version française 🇫🇷

## Exigences

### Python

Tout d'abord, vous devez avoir Python 3 (ou une version supérieur) d'installé. Si vous ne l'avez pas, installez-le simplement via la [page d'installation de Python](https://www.python.org/downloads/).

### Discord.py

Ensuite, installez discord.py qui est nécessaire pour faire fonctionner votre bot :

```
pip install discord-py
```

## Créer un bot

1) Allez d'abord sur le [Portail des développeurs Discord](https://discord.com/developers/applications)
2) Cliquez ensuite sur "Nouvelle application" en haut à droite, et donnez-lui un nom (le nom n'a pas vraiment d'importance)
3) Allez dans OAuth2
4) Cochez `bot` et `applications.commands`
5) Faites défiler jusqu'à `BOT PERMISSIONS`
6) Cochez `Administrateur`
7) Copiez l'URL générée et collez-la dans votre navigateur
8) Ajoutez le bot à votre serveur. RECOMMANDÉ : vous pouvez créer un nouveau serveur pour cela, et en faire un serveur Communautaire (ce qui sera nécessaire pour réclamer le badge)
9) Retournez au Portail des développeurs Discord, et allez dans `Bot`
10) Décochez `PUBLIC BOT` et cochez toutes les Intents (`PRESENCE INTENT`, `SERVER MEMBERS INTENT`, `MESSAGE CONTENT INTENT`)
![intents à cocher](screens/intents.png)
11) Appuyez sur le bouton `Réinitialiser le jeton` et copiez votre jeton de bot (⚠️ ne le partagez **PAS** avec qui que ce soit)
12) Enfin, allez dans le fichier `bot.py` et collez-le dans les parenthèses de `bot.run("VOTRE JETON")`

### Réclamer le badge

Après avoir utilisé la commande /hello, vous devrez attendre au moins 24 heures pour pouvoir réclamer votre badge sur [Badge de développeur actif](https://discord.com/developers/active-developer).

> [!IMPORTANT]
> La commande /hello peut ne pas être disponible immédiatement après le démarrage du bot. Cela peut prendre jusqu'à une heure pour devenir accessible.
