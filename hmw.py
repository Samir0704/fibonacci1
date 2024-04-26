

def PrintFibonacci(length):
    # Asosiy holat uchun boshlang'ich o'zgaruvchi
    first = 0
    second = 1

    # Dastlabki Fibonachchi raqamini chop etish
    print(first, second, end=" ")

    # uzunligi ikkiga qisqaradi, chunki birinchi 2 Fibonachchi raqamlari
    # allaqachon chop etilgan
    length -= 2

    # Uzunlik 0 ga teng bo'lguncha aylantiriladi
    while length > 0:
        # Keyingi Fibonachchi raqamini chop etish
        print(first + second, end=" ")

        # Keyingi raqamni topish uchun birinchi va ikkinchi o'zgaruvchilarni yangilanadi
        temp = second
        second = first + second
        first = temp
        length -= 1


if __name__ == "__main__":
    print("Fibonacci  - ")
    PrintFibonacci(12)
    pass


# import psycopg2
#
# host = 'localhost'
# user = 'postgres'
# password = '1'
# database = 'n42'
# port = 5432
#
# conn = psycopg2.connect(host=host,
#                         database=database,
#                         user=user,
#                         password=password,
#                         port=port
#                         )
# cur = conn.cursor()
# insert_car_query = """
#     insert into cars(name,color,item_id)
#     values('Ferrari','Yellow',3)

