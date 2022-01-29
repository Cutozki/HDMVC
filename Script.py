class script(object):
    START_TXT = """<b>Hello {}</b>
<i>Iam A Simple Auto Filter + Movie Search + Manual Filter Bot. I Can Provide Movies In Telegram Groups. I Can Also Add Filters In Telegram Groups.  Just Add Me To Your Group As Admin And Enjoy</i>
<b>Made With ❤ BY @IET_Updates</b>"""
    HELP_TXT = """<b><i>Here is the help menu</i></b>"""
    ABOUT_TXT = """<b>🤖 ʙᴏᴛ ɴᴀᴍᴇ: <a href= https://t.me/MinnalsMuraliBot>🦸 Mɪɴɴᴀʟ Mᴜʀᴀʟɪ</a></b>
 
<b>📝 ʟᴀɴɢᴜᴀɢᴇ :</b><b> <a href= https://www.python.org/>ᴘʏᴛʜᴏɴ³</a></b> 
<b>📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ :</b><b> <a href= https://docs.pyrogram.org/>ᴘʏʀᴏɢʀᴀᴍ</a></b>
<b>📡 ʜᴏsᴛᴇᴅ ᴏɴ :</b><b> <a href= https://www.heroku.com/>ʜᴇʀᴏᴋᴜ</a></b>
<b>👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b><b> <a href= https://t.me/Iqbal_KA>Iǫʙᴀʟ ᴋ ᴀ</a></b>
<b>💡 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :</b><b> <a href= https://t.me/IET_Owner/724>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>
<b>👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :</b><b> <a href= https://t.me/IET_SUPPORT>ɪᴇᴛ sᴜᴘᴘᴏʀᴛ</a></b>
<b>📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ :</b><b> <a href= https://t.me/IET_Updates>ɪᴇᴛ ᴜᴘᴅᴀᴛᴇs</a></b>"""
    SOURCE_TXT = """<b>🎈</b>
<b><u>📽️ How To Create This BoT.?</u></b>
<i><a href= https://youtu.be/1ltbuCY_V6s>എങ്ങനെ ഉണ്ടാക്കാം എന്ന് അറിയാൻ ഇവിടെ ക്ലിക്ക് ചെയ്താൽ മതി.</a></i>
<b>Support channel:</b>
- <a href=https://t.me/IET_support>IET SUPPORT</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. BoT should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    FILTER_TXT = """𝖲𝖾𝗅𝖾𝖼𝗍 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋 𝗍𝗒𝗉𝖾 𝖻𝖾𝗅𝗈𝗐:"""
    TRSLT_TXT = """Here is the help for the <b>Translator</b> module:
Use this module to translate stuff... duh!

<b>Commands:</b>
• <code>/tl</code> (or <code>/tr</code>): as a reply to a message, translates it to English.
• <code>/tl <lang></code>: translates to <lang>
  eg: <code>/tl ja</code>: translates to Japanese.
• <code>/tl <source>//<dest></code>: translates from <source> to <lang>.
  eg: <code>/tl ja//en</code>: translates from Japanese to English.
• <code>/langs</code>: get a list of supported languages for translation."""
    MISC_TXT = """<b>Misc</b>

An "odds and ends" module for small, simple commands which don't really fit anywhere.

<b>Commands</b>:
- /runs: Respond with a randomly generated "run away" string.
- /id: Get a user's ID.
- /info: Get a user's info.
- /donate: Donate to the bot creator.
- /markdownhelp: Information on how to use markdown with the bot. PM only."""
    MUT_TXT = """Here is the help for the <b>Muting</b> module:
<b>Admins only:</b>
 • <code>/mute (userhandle)</code>: silences a user. Can also be used as a reply, muting the replied to user.
 • <code>/tmute (userhandle) x(m/h/d)</code>: mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
 • <code>/unmute (userhandle)</code>: unmutes a user. Can also be used as a reply, muting the replied to user."""
    REPOT_TXT = """<b>Reports</b>

We're all busy people who don't have time to monitor our groups 24/7. But how do you react if someone in your group is spamming?

Presenting reports; if someone in your group thinks someone needs reporting, they now have an easy way to call all admins.

<b>User commands:</b>
- /report: Reply to a message to report it for admins to review.
- admin: Same as /report

<b>Admin commands:</b>
- /reports <code><yes/no/on/off></code>: Enable/disable user reports.

To report a user, simply reply to his message with @admin or /report; Bot will then reply with a message stating that admins have been notified. This message tags all the chat admins; same as if they had been @'ed.

Note that the report commands do not work when admins use them; or when used to report an admin. Bot assumes that admins don't need to report, or be reported!"""
    FUN_TXT = """Here is the help for the <b>Fun</b> module:
• /runs: reply a random string from an array of replies.
• /pat: pat a person, cool thing to have for cute ones :3
• /slap: slap a user, or get slapped if not a reply.
• /shrug : get shrug XD.
• /table : get flip/unflip :v.
• /decide : Randomly answers yes/no/maybe
• /toss : Tosses A coin
• /roll : Roll a dice.
• /rlg : Join ears,nose,mouth and create an emo ;-;
• /shout <keyword>: write anything you want to give loud shout.
• /stickerid: reply to a sticker to get its ID.
• /getsticker: reply to a sticker to get the raw PNG image.
• /steal: reply to a sticker or image to add it to your pack."""
    NOTE_TXT = """Notes

Save data for future users with notes!

Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!

<b>User commands:</b>
- /get <notename>: Get a note.
- #notename: Same as /get.

<b>Admin commands:</b>
- /save <notename> <note text>: Save a new note called "word". Replying to a message will save that message. Even works on media!
- /clear <notename>: Delete the associated note.
- /notes: List all notes in the current chat.
- /saved: Same as /notes.
- /clearall: Delete <b>ALL</b> notes in a chat. This cannot be undone.
- /privatenotes: Whether or not to send notes in PM. Will send a message with a button which users can click to get the note in PM."""
    PARGE_TXT = """<b>Purges</b>

Need to delete lots of messages? That's what purges are for!

<b>Admin commands:</b>
- /purge: Delete all messages from the replied to message, to the current message.
- /purge <X>: Delete the following X messages after the replied to message.
- /spurge: Same as purge, but doesnt send the final confirmation message.
- /del: Deletes the replied to message.
- /purgefrom: Reply to a message to mark the message as where to purge from - this should be used followed by a /purgeto.
- /purgeto: Delete all messages between the replied to message, and the message marked by the latest /purgefrom.

<b>Examples:</b>
- Delete all messages from the replied to message, until now.
-> /purge
- Mark the first message to purge from (as a reply).
-> <code>/purgefrom</code>
- Mark the message to purge to (as a reply). All messages between the previously marked /purgefrom and the newly marked /purgeto will be deleted.
-> /purgeto"""
    AFK_TXT = """Here is the help for the <b>AFK</b> module:
- /afk <reason>: mark yourself as AFK(away from keyboard).
- brb <reason>: same as the afk command - but not a command.
When marked as AFK, any mentions will be replied to with a message to say you're not available!"""
    LOKE_TXT = """<b>Locks</b>

Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!

The locks module allows you to lock away some common items in the telegram world; the bot will automatically delete them!

<b>Admin commands:</b>
- /lock <item(s)>: Lock one or more items. Now, only admins can use this type!
- /unlock <item(s)>: Unlock one or more items. Everyone can use this type again!
- /locks: List currently locked items.
- /lockwarns <yes/no/on/off>: Enabled or disable whether a user should be warned when using a locked item.
- /locktypes: Show the list of all 
- /allowlist <url/id/@channelname(s)>: Allowlist a URL, group ID, channel @, or bot @ to stop them being deleted by URL, forward, invitelink, and inline locks.
- /rmallowlist <url/id/@channelname(s)>: Remove an item from the allowlist - url, invitelink, and forward locking will now take effect on messages containing it again.
- /rmallowlistall: Remove all allowisted items."""
    BUTTON_TXT = """Help: <b>Buttons</b>

- This BoT Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/IET_UPDATES)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    IMDB_TXT = """<b>This BoT Supports  IMDB Informations</b>

<u>Available vars</u>
query = searched movie name
title = original imdb title
localized_title = local name of movie
rating = imdb Rating
votes = number of votes on which rating is based.
imdb_id =imdb Id 
poster = url of imdb poster
url = imdb url
plot = story line
runtime = runtime info in minutes
release_date = date of release if available , else year
year = year of release
Etc...

<b>💡How to Get </b>

/imdb  - get the film information from IMDb source."""
    BATCH_TXT = """HOW TO USE 🤔?
📍 You have two options.

<i>1. You can use the filestore feature for any public channel without bot being admin in that channel (only media messages  can be stored).</i>

<i>?. What if the channel owner delete those files?
Still your bot can serve you the files from the links it generated.</i>

<i>2. You will have to add the bot to your channel as admin and add the channel ids in config vars as FILE_STORE_CHANNEL (Multiple channel ids are supported, separate each of them by a space)</i>

How to generate links? 🙄

1. For a single file use /link command as reply to file.(only video, audio and documents are supported for now.)

2. For creating batch files , use /batch <starting message link> <ending message link>.
Example: /batch https://t.me/iet_updates/2 https://t.me/iet_updates/9"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """<i>Here is the</i> <b>Extra Modules</b> <i>menu</i>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>📁 ᴛᴏᴛᴀʟ ꜰɪʟᴇs: {}</b>
<b>👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: {} 🕸️</b>
<b>👥 ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: {} 🕷️</b>
<b>⚙️ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: {}</b>
<b>🆓 ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ: {}</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
