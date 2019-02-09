from pypika import Query, Table, Field, Order, Tables

def main():
    customers = Table('customers')
    q = Query.from_(customers).select(
        customers.id,customers.fname
    ).where(
        customers.age[18:65] & customers.status.isin(['new', 'active'])
    )
    print(q.get_sql())

if __name__ == '__main__':
    main()