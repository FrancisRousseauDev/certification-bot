import psycopg2
from discord.ext import commands
import discord
import drawer
import io
import os
import json

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')
client = discord.Client()
dictOfAddresses = {}
started = False
questionNumber = 0
name = ''
personal = ''
allEarly = ['0x5f1372d1114b1fe0fc81f193096496f01edf17be' ,'0xCD90d9bA0060937c442C5560055a785Ed428E1F9', '0x5f1372d1114b1fe0fc81f193096496f01edf17be', '0x4962d58f07db543a64dc9ceae959c55f451db042', '0xc28251ffe4187e8fba30b03f960cf42d772b0e73', '0x344e6561b01179d12f313bfd214ab425f02af210', '0x00337efdc08921773fefc799f7eed059e48f8ee3', '0x3fe9a96c00a7a080e532a93bd880615f38553769', '0xd4bc6591ab32ef268feae542c8d0e7ab2ad122d1', '0xcd90d9ba0060937c442c5560055a785ed428e1f9', '0xc6976223f1a3c314ac9df2a799da26a7c9db1fbc', '0xa217575283b35d5924552e20e08542f7b4eb7799', '0x6ec6747014b052269a27bab2b5e279aaf800b503', '0x42ab5fd8f56aa34f0a635258b83b3ab6dbc16a19', '0x1f447496e6ab32c395cf69753407bd0d2d688d58', '0xc8dfe7d82fb842b5e76791f6a2d5074c14fd4462', '0x308a556cd21ad70727ce84563020c50d4bc54858', '0x047de46b890d00fac1b34cad24fba8455136dd49', '0x70e93d45290399c19666f589059773dd0e339403', '0xb62d09ae5205fcda55c7ca6eb49543dcaa9af7eb', '0x74516cb07eea29a814437894bc5a2d24defd9c20', '0x46d00b135035566b86375480bf4d932f6c43cd98', '0x94c75cc593fa085b8c275992de7d1f12fb161b93', '0x76019eb2fbccc93750ae68bb83abf2af08e4d322', '0xbcd6e1d47a08e9cb053f38b3f0018cf553ccf3d6', '0x8f43e4a58beb426c15beb98f84452bfec46e4a3b', '0x7ccadeea14dd6727845b58f8aa7aad0f41a002a2', '0x1ff2d6c0daf8363189240f1bb8f9df1cab162ab3', '0xd6fe01d5f3ce9f77780468bc9f397f32d6cd90ed', '0x08da0b97a6d34195c1db166235d72a0322b2b425', '0x4c0df563416f0ff7242a7ab4fe59c79ace52877b', '0x3f7fc5dba955fe4877ab06596ea669f6006f8a09', '0xaad5e0e9982cc8ba4e67121d76784369068897b8', '0x9b4117af35a8800723101299d23d17d74487b27d', '0x7720ae3685b2e1567353c55fcce0318fb6b44ef9', '0x97e3288048a9b38d6a73de74c27fecf6880b9f67', '0x2a8cc6d13980e90388ee7595161cd0bd02046c96', '0xd3773f092e22b151b1943957c46beaeb999f2a40', '0x41bb2b3107269f26f1bdc47ab3c2da2e98bf668c', '0xb2ae35d94a79c816faacc71f17d9a65b88afcb73', '0x01e8c0ebae7d3eb0087337e43c92079914bc009e', '0x8d7279f08bc38cc422eb355a56be46e59dceea48', '0x048f7a02f59d648f2195811a9d8e3c2849f54930', '0xeb62df4e9d9674a42127f00a5b3ede72dccdaa72', '0x9b2e496403dd86e5380ad65a6699fa55ddabfce2', '0x4d638656c9de316398281a0b790779fc399b4df7', '0xe1971a640e443b737a6788f59b9ee8b5ea855b82', '0xbeb29348ffa412aa66ce88410df3408bcc1351b1', '0x7c05bbd53ce7c4f1ef60a8510ead673920d9ba08', '0xe1fef2a18236763e24824566e4a71791741a44e8', '0xbee8bf75016dc7f9cbfaacef7bb610a3014bea1c', '0x1d77cb8b8585585faaf6c2c9d336868f173b1423', '0x717d11ddbf51d70e3e3c25db75ba6c3002aa12cf', '0xbdbd5c71c51aae80fc3d8427923bc2f5fe4381e1', '0xf47e64ead02777837ac695d210444b8447cca7c6', '0x052182ee1e77daf5f36ff34781dc8fba49808c5e', '0x55d6abae3910446a6bbeafaa221b9d7e846ee68b', '0x806d678963caebd1b8153a6e823e8876923cd37c', '0x9cd315551c2f96bb978ed24687f6cea6b4097995', '0x66d85903961f0dec5a3ffa7dd3681c0ec7a1594d', '0x1c8192c2a0f563cc37c394196362583cf719307e', '0xdba673b14cb4c283a9cc13a640ef3b62b100d98b', '0xcf67cf843c9ea6bed48a205670c528abada00b10', '0x599eaf47240d70f419472ee981e63c23e23cf548', '0x6333439fa7dd71c9b232f9c76c3ee74e05267aae', '0x1dd49ddaebfd8cda77c8d60ee57f988081d9db54', '0x00d906fb159935ad8f18414760655c5bbfea1118', '0x52f95613130c07f0efdb21b263f3fb84df3e77c5', '0x637a47b6778dbcb14802c00bc116ed229c6aebf1', '0x2bde762da985417ae46784b06e6ac160f73d73c6', '0x74b97ec3a9cf2a93667ad97ae2a2ed5cd6c9d983', '0x9a6cf8cb187241351afcae1f09c174f6fefd9ea7', '0x40ecba12536be45c4f45c5c617a2b21167de3ad3', '0x4312c9c70ffe1fdece8a5a7ec481cab2fe3e4459', '0xaa14b1ef279a43e6e327766dd2b8bd31687b94d0', '0x62fe7d6ef4fa2c978bff116ab337651709d6f4e4', '0x1d88a45518a7803a36af899351f030832094df75', '0xa6c7ea95ed282f9ed5c754bbe8be22bc74eee19c', '0xca2e9035e3cce48fe2f2e3ef7b527953092eacf5', '0x1a3b2ec1fcd0801d414bdd8f2eb1154d72bca437', '0xd650fddd1f9b220d69c50e4014a168c10a934695', '0x7a85a344d7fc6aeac7551f9f5b4c00c0346d8095', '0x221008a166395a85ff3114967303f62b247b5544', '0x1cd81ec753a12a274715e03a09c0618a18b6f4d3', '0x0c0cd1e907b0a85ac02e4f791fbdcabb7c29962d', '0x134c2581b839f8b4576745133a51a46b49d150aa', '0x9f7dcf5309d3084d1087adb86fb4fe53f5c013b7', '0x5fc495ff97d5dba3404db656437d01a3873f5aa3', '0xf780722299993c9c6ca401621e81f50696cc4c89', '0xbf272c23cca9a5cd9c354e27306b3904d2828f1e', '0x43d9063766eeab9664ae43b3c42c5dee5b30bac8', '0xe627cc4e57c1af653aec09631412f619438a805c', '0xea921efa7693743e1df67b21241b35055f4c6623', '0xfcb2501292ff607329d1c71c0d4d501dbcc046ba', '0x018c45dbcde8630854d586ebeb3695611d5f0fdf', '0xf5580989aaa868e5931a316a6a7ffc42700474ea', '0x3eaaf037f965e2d77fa0d8d9b0288f26175cd750', '0x8c7b9e5fdd8d31af8c859e04633e37c4d242243f', '0xfc7f42c3f084bda5b15c58e1fc7e5274107c8992', '0x2fc761e8b14005f45276e7b0e73008909049aca5', '0x39473c4d9226ef674b70f4aac89a06c29c474501', '0xe12f38c377074e0ac70f7f56434b8e2e9c7d4f06', '0x1bfd6651f697513bc6e8394a0d84fc78bab0eb69', '0xb4e7e5ef8fb46ddc90a3f4888a1855aee8bb6a2c', '0xea78a76e0918414c818f90c0693384951f5e2f04', '0x1218d1dc6a0e7c0a71b40552f59c7b0df4e880c7', '0xd07d266a7407118c48afe4f4e12ef24ea4d49971', '0xa5c43e48d8ae426b40e31c507bb40bc9133abb60', '0x8a485606d7b9da68b0ad8f14a987b6741b1716f8', '0xeda68adb283c8b38e8f20aa3cbde76232d7256c5', '0x6c99b8ef77b6e7b7071f524492841c6db943aad7', '0xe3613bb4c027dc0fc3665ae8dc9892b1face5708', '0xff46862d6dcead9042600b278e9bfd17c61cceb6', '0x7d4be433a114f2b2ef382db9a6af4662ceacfe5d', '0x420ff19a7ed3330bb66f02811f5fbcbbc30c337e', '0x66d3418b697a57228835e17f3793a1dddfb16253', '0xd39a533791244953bc7d745e8693886a8d68b290', '0x2e0b8ad311ed11a9f02331951c3c2f282f621f36', '0x2a64835eaf941546b5aadc23fb34e34fea16b204', '0x5ec64708d2d0751c49e71b935257512282b1a244', '0x3701ce7bbb4b84cb1ae1f3061a438f2ad3384a25', '0x53f61153b1bc36327c5719114e7f5fd73cfcdf1f', '0xe27dd9577b8cadf41e8a99744cc0df071b222114', '0x1cae9c65c0f2a5a3ebebaf819ba2cba9a583a9f9', '0xde98ce6eedbb4a2017b0311afabc2096d5fae7f5', '0x9ca36ce6d388b5a7bc96b97b1520ebe06ddd0486', '0x8bc1ea406ba331f0b139cc5f1b4305ae174f5063', '0xaee087732f2c4a81e13f08ced9933f825c1daf6a', '0x529db6f8eab91a051956b7fd82a25a66d34644a2', '0x0660663c630f43f4a8df1448e6c6157f8b91e817', '0x5991ad68745c0974d70e6f6ae9ecc64463cbb396', '0x1aa40fc2c7ab1c040cccb31e3d8ceae4fc847da3', '0xfa7df185dce84bcd089b1be1b73775079fc3572d', '0xbcdfdbd6341cfeb5d86158b5d9252f333cb6109e', '0x9a0f5d535f63072df09a5456cd0b47925238310b', '0x6dc942b7acdd253e663bcedc7d7a2bd667a3e28f', '0x64e654f0be231b28728eca495d56a9891775880d', '0xa680b6af31a3e70279ac38681261eafbda462ef1', '0x87124d250603f40b0c4c31e0e628ebe481bda200', '0x9036867f0df93f8866970fce362b531cc7a0e5ea', '0x6e2f52ecd3f99c537a06d0c5761ca59eea25598d', '0x950691efb9fba67dbd987e36e0c6ae840f9d7bb0', '0x573311ed8a571df948ebd4f54a053b9f70509637', '0x215d8de8e3f3b57649617f3bfdab380038507636', '0x7b2c3375f7cf565e88adef6d3685a3550f0d4bf1', '0x1b4e3f90320a8b0022e6be44275e2e49d30aa2fc', '0xaa9cdb75944cc86d2ac526f5aa12b06584f0417b', '0x47eb632bb439988790495e4c0514cee5c1e4ef87', '0xb362d59059d867ad1fe4ef433cf732931ea382e0', '0x422b65dcb4ff4f48b68f012aed28613cd46621b8', '0x414109d3a9fa9803498c79616a40473f3a428a24', '0xf0bc5aec07df1439203111c3b238f4469b0f6a8e', '0x8fbe80d32f5d3aaaeb4166caa36ffaee7215dc10', '0x721CAb3C58d2Cc8899b1e658bF6d9dFBa1d49ee2', '0x1bcf09e6b12427f17c9cf7c464e105b71863b792', '0x78c59058cb365041045ea9ede59d2e7585c57c7d', '0xfd1a2a68c7244b879a72b2761da2ea4a247bcf6e', '0xc494b8efbb9dfa70b758ec8f145849aeb9cdc530']


@client.event
async def on_message(message):
    global started
    global dictOfAddresses
    global name
    global wallet
    global personal
    global questionNumber
    global allEarly

    if str('958030087553417277') in str(message.author.id):
        return
    if message.guild:
        if not str('958030087553417277') in str(message.author.id):
            if message.content == '!!start':
                await message.channel.send(errorMessage())
                return
            else:
                return

    if message.content == '!!reset':
        readDatabase('delete', message.author.id, message.author.name, '', 'unknown', 'unknown')
        await message.channel.send(embed=getMessageReset())

    if message.content == '!!start':
        response = readDatabase('check', message.author.id, '', '', '', '')
        if not len(response) > 0:
            await message.channel.send(embed=getInfoMessage())
            await message.channel.send(file=discord.File("prev.jpg"))
            await message.channel.send(embed=getWalletAddress())
            started = True
        else:
            name = response[0][2]
            personal = response[0][3]
            wallet = response[0][4]
            await alreadyFinished(message)
    elif started and questionNumber == 0:
        wallet = message.content
        if wallet.lower() in [x.lower() for x in allEarly]:
            readDatabase('set', message.author.id, message.author.name, 'unknown', 'unknown', wallet)
            questionNumber = questionNumber + 1
            await message.channel.send(embed=getCertName())
        else:
            questionNumber = 0
            started = False
            await message.channel.send(embed=notEarlyBird())

    elif started and questionNumber == 1:
        name = message.content
        questionNumber = questionNumber + 1
        await message.channel.send(embed=getPersonalMessage())
    elif started and questionNumber == 2:
        personal = message.content
        await finished(message)

def notEarlyBird():
    embed = discord.Embed(title="Your wallet address is not registered as an early holder!",
                          color=discord.Color.red())
    embed.set_author(name="Retry in correct format",
                     icon_url="https://vesea.mypinata.cloud/ipfs/QmRcHAUzrrDWgveWmbBrqJaSivpnhaPiCL2sWEigScaDJt/2.jpg")
    embed.set_thumbnail(
        url="https://s3.us-east-2.amazonaws.com/vesea.io-assets/images/collections/veeparrots/banner.png")
    return embed

def errorMessage():
    error = f"Please send me in private!"
    return error


def getInfoMessage():
    welcomeMessage = f"\nWelcome to the Certification bot!\n" \
                     "\n" \
                     "First of all, we would like to thank all of you who patiently await the future of our beloved VeeParrots! It seems like some of you are very eager to spread their wings 😉🦜\n" \
                     "\n" \
                     "This bot will automise the customisation and delivery of your certificate together with your poster. (see examples below)\n_" \
                     "To get started fill in your wallet-ID below first to verify if you're an early holder" \
                     "Only holders who obtained their parrot before 28 februari 2022 16:00 are eligible to request both their certificate and poster\n" \
                     "\n" \
                     "_Please see following example:"
    embed = discord.Embed(
        title="Welcome to the VeeParrots certification bot",
        description="_This bot will automise the customisation and delivery of your certificate together with your poster. (see examples below)_",
        color=discord.Color.blue())
    embed.set_author(name="VeeParrots certification bot",
                     icon_url="https://vesea.mypinata.cloud/ipfs/QmRcHAUzrrDWgveWmbBrqJaSivpnhaPiCL2sWEigScaDJt/2.jpg")

    embed.set_thumbnail(url="https://s3.us-east-2.amazonaws.com/vesea.io-assets/images/collections/veeparrots/banner.png")

    embed.add_field(name="Intro", value="First of all, we would like to thank all of you who patiently await the future of our beloved VeeParrots! It seems like some of you are very eager to spread their wings 😉🦜", inline=False)
    embed.add_field(name="Start", value="To get started fill in your wallet-ID below first to verify if you're an early holder", inline=False)
    embed.add_field(name="Condition", value="Only holders who obtained their parrot before 28 februari 2022 16:00 are eligible to request both their certificate and poster", inline=False)

    return embed

def getWalletAddress():
    embed = discord.Embed(title="What is your wallet address?",
        color=discord.Color.blue())
    embed.set_author(name="Question",
                     icon_url="https://vesea.mypinata.cloud/ipfs/QmRcHAUzrrDWgveWmbBrqJaSivpnhaPiCL2sWEigScaDJt/2.jpg")

    embed.set_thumbnail(
        url="https://s3.us-east-2.amazonaws.com/vesea.io-assets/images/collections/veeparrots/banner.png")
    return embed

def getCertName():
    embed = discord.Embed(title="What's the name you want to displayed on your certificate?",
                          color=discord.Color.blue())
    embed.set_author(name="Question",
                     icon_url="https://vesea.mypinata.cloud/ipfs/QmRcHAUzrrDWgveWmbBrqJaSivpnhaPiCL2sWEigScaDJt/2.jpg")

    embed.set_thumbnail(
        url="https://s3.us-east-2.amazonaws.com/vesea.io-assets/images/collections/veeparrots/banner.png")
    return embed

def getPersonalMessage():
    embed = discord.Embed(title="What's the personalised message you want to display on your certificate?",
                          color=discord.Color.blue())
    embed.set_author(name="Question",
                     icon_url="https://vesea.mypinata.cloud/ipfs/QmRcHAUzrrDWgveWmbBrqJaSivpnhaPiCL2sWEigScaDJt/2.jpg")

    embed.set_thumbnail(
        url="https://s3.us-east-2.amazonaws.com/vesea.io-assets/images/collections/veeparrots/banner.png")
    return embed

def getMessageReset():
    embed = discord.Embed(title="You have succesfully reset your address!",
                          color=discord.Color.red())
    embed.set_author(name="Reset",
                     icon_url="https://vesea.mypinata.cloud/ipfs/QmRcHAUzrrDWgveWmbBrqJaSivpnhaPiCL2sWEigScaDJt/2.jpg")
    embed.set_thumbnail(
        url="https://s3.us-east-2.amazonaws.com/vesea.io-assets/images/collections/veeparrots/banner.png")
    return embed

async def alreadyFinished(message):
    global name
    global personal
    global questionNumber
    global wallet
    questionNumber = 0
    embed = discord.Embed(title="You already saved your details!", description="You can use the command: *!!reset* to start over",
                          color=discord.Color.red())
    embed.set_author(name="Oops",
                     icon_url="https://vesea.mypinata.cloud/ipfs/QmRcHAUzrrDWgveWmbBrqJaSivpnhaPiCL2sWEigScaDJt/2.jpg")

    embed.add_field(name="Wallet",
                    value=wallet,
                    inline=False)
    embed.add_field(name="Name",
                    value=name,
                    inline=False)
    embed.add_field(name="Message",
                    value=personal,
                    inline=False)

    embed.set_thumbnail(
    url="https://s3.us-east-2.amazonaws.com/vesea.io-assets/images/collections/veeparrots/banner.png")
    await message.channel.send(embed=embed)
    await sendReadyImage(message)
    await message.channel.send(file=discord.File("poster.jpg"))


async def sendReadyImage(message):
    global name
    global personal
    image = drawer.getImage(name, personal)
    with io.BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.channel.send(file=discord.File(fp=image_binary, filename='image.png'))

async def finished(message):
    global questionNumber
    questionNumber = 0
    readDatabase('update', message.author.id, message.author.name, name, personal, wallet)
    embed = discord.Embed(title="Info", description="Your personalised VeeParrots certificate together with poster are available for download over here:",
                          color=discord.Color.blue())
    embed.set_author(name="Thank you " + name,
                     icon_url="https://vesea.mypinata.cloud/ipfs/QmRcHAUzrrDWgveWmbBrqJaSivpnhaPiCL2sWEigScaDJt/2.jpg")

    embed.set_thumbnail(
        url="https://s3.us-east-2.amazonaws.com/vesea.io-assets/images/collections/veeparrots/banner.png")

    await message.channel.send(embed=embed)
    await message.channel.send(file=discord.File("poster.jpg"))
    await sendReadyImage(message)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


def readDatabase(type, discordId, discordName, certName, certMessage, walletAdress):
    global connection
    try:

        connection = psycopg2.connect(user=os.getenv('USER'),
                                      password=os.getenv('PASSWORD'),
                                      host=os.getenv('HOST'),
                                      port=5432,
                                      database=os.getenv('DATABASE'))
        cursor = connection.cursor()

        result = ''
        if type == 'check':
            query = 'SELECT "certification"."discordID", "certification"."discordName", "certification"."certName", "certification"."certMessage", "certification"."walletAdress" FROM public.certification where "certification"."discordID" = \'' + str(
                discordId) + '\''
            cursor.execute(query)
            result = cursor.fetchall()

        if type == 'delete':
            print(discordId)
            query = 'DELETE FROM public.certification where "certification"."discordID" = \'' + str(discordId) + '\''
            cursor.execute(query)
            connection.commit()

        if type == 'set':
            postgres_insert_query = """ INSERT INTO public.certification("discordID", "discordName", "certName", "certMessage", "walletAdress") VALUES (%s, %s, %s, %s, %s)"""
            record_to_insert = (discordId, discordName, certName, certMessage, walletAdress)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            result = cursor.rowcount

        if type == 'update':
            postgres_insert_query = """ UPDATE public.certification SET "certName"=(%s), "certMessage"=(%s), "walletAdress"=(%s) WHERE "certification"."discordID" = (%s);"""
            record_to_insert = (certName, certMessage, walletAdress, str(discordId))
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            result = cursor.rowcount

        print('res', result)
        return result


    except (Exception, psycopg2.Error) as error:
        print(error)
        return str(error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()

client.run(TOKEN)
