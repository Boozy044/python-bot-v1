from databases import Database
import config

database = Database(f'mysql+aiomysql://{config.USER}:{config.PASSWORD}@{config.HOST}/{config.DATABASE}')


async def get_answer(question):
    try:
        await database.connect()

        corrective = await database.fetch_one(query=f"SELECT t1.corrective FROM questions t1 WHERE t1.question = '{question}';")

        if corrective:
            query = f"""SELECT t2.answer FROM questions t2 WHERE t2.corrective = '{corrective[0]}' AND t2.answer != '' LIMIT 10;"""
        else:
            corrective = ['']
            query = f"""SELECT t6.kart FROM kart t6 WHERE t6.kart LIKE '%{question}%' AND t6.aktual = '1' LIMIT 10;"""

        result = await database.fetch_all(query=query)
        return corrective, result

    except Exception as ex:
        print(ex)

    finally:
        await database.disconnect()


async def get_not_answer():
    try:
        await database.connect()

        query = f"SELECT t3.answer FROM questions t3 WHERE t3.question = 'NOT_FOUND' LIMIT 1"
        result = await database.fetch_all(query=query)
        return result[0]

    except Exception as ex:
        print(ex)

    finally:
        await database.disconnect()


async def make_logs(id, full_name, question, answer, corrective):
    try:
        await database.connect()

        query = f"INSERT INTO `logs`(`channel`, `user_id`, `full_name`, `question`, `corrective`, `answer`) VALUES ('Telegram', '{id}', '{full_name}', '{question}', '{corrective}', '{answer}')"
        await database.execute(query=query)

    except Exception as ex:
        print(ex)

    finally:
        await database.disconnect()


async def get_buttons():
    try:
        await database.connect()

        query = f"SELECT t1.answer FROM questions t1 WHERE t1.question = '__Кнопка';"
        result = await database.fetch_all(query=query)
        return result

    except Exception as ex:
        print(ex)

    finally:
        await database.disconnect()