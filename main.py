import streamlit as st
import mysql.connector
import pandas as pd
# Function to create a connection to MySQL
def create_connection():
    return mysql.connector.connect(
        host="localhost",  # Change this to your MySQL server if it's not local
        user="root",
        password="raja",
        database="retailanalysis"
    )


# Connect to MySQL
conn = create_connection()

#st.title("_Retail order Analysis_")
st.markdown(
    '<h1 style="text-align: center;"><p style="font-size:50px; font-style:italic; color:purple;">Retail order Analysis</p></h1>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1],gap="small",border=True)

with col1:
    
    st.write("**Analysis 10 Questions given in the project**")
    st.markdown("---")
    st.write("**_1.Find top 10 highest revenue generating products_**")

    # Example query to fetch data from the database
    cursor = conn.cursor()

    # Execute the query
    cursor.execute("SELECT product_id, SUM(discounted_price) AS sales FROM orders GROUP BY product_id ORDER BY sales DESC LIMIT 10;")

    # Fetch all results
    table1 = cursor.fetchall()

    # Convert results to a pandas DataFrame, using the correct 'columns' argument
    answer_1 = pd.DataFrame(table1, columns=['product_id', 'sales'])

    if st.button("1.Answer"):
        st.dataframe(answer_1)

    st.write("**_2.Find the top 5 cities with the highest profit margins_**")

    # Execute the corrected SQL query
    cursor.execute("SELECT city, SUM(profit) AS profitmargin FROM orders GROUP BY city ORDER BY profitmargin DESC LIMIT 5;")

    # Fetch all results
    table2 = cursor.fetchall()

    # Convert results to a pandas DataFrame, using the correct column names
    answer_2 = pd.DataFrame(table2, columns=['city', 'profitmargin'])

    # Display the DataFrame
    if st.button("2.Answer"):
        st.dataframe(answer_2)

    st.write("**_3. Calculate the total discount given for each category_**")
    cursor.execute("SELECT category, SUM(discount) AS total_discount FROM orders GROUP BY category ORDER BY total_discount DESC LIMIT 3;")

    table3 = cursor.fetchall()

    answer_3 = pd.DataFrame(table3, columns=['category', 'total_discount'])

    if st.button("3.Answer"):
        st.dataframe(answer_3)

    st.write("**_4.Find the average sale price per product category_**")

    cursor.execute("SELECT category, avg(discounted_price) AS ave_price FROM orders GROUP BY category;")

    table4 = cursor.fetchall()

    answer_4 = pd.DataFrame(table4, columns=['category', 'ave_price'])

    if st.button("4.Answer"):
        st.dataframe(answer_4)

    st.write("**_5.Find the region with the highest average sale price_**")
    cursor.execute("SELECT region, avg(discounted_price) AS region_price FROM orders GROUP BY region;")

    table5 = cursor.fetchall()

    answer_5 = pd.DataFrame(table5, columns=['region', 'region_price'])

    if st.button("5.Answer"):
        st.dataframe(answer_5)

    st.write("**_6.Find the total profit per category_**" )

    cursor.execute("SELECT category, sum(profit) AS total_profit FROM orders GROUP BY category;")

    table6 = cursor.fetchall()

    answer_6 = pd.DataFrame(table6, columns=['category', 'total_profit'])

    if st.button("6.Answer"):
        st.dataframe(answer_6)

    st.write("**_7.Identify the top 3 segments with the highest quantity of orders_**")

    cursor.execute("SELECT segment, sum(quantity) AS total_segment FROM orders GROUP BY segment;")

    table7 = cursor.fetchall()

    answer_7 = pd.DataFrame(table7, columns=['segment', 'total_segment'])

    if st.button("7.Answer"):
        st.dataframe(answer_7)

    st.write("**_8.Determine the average discount percentage given per region_**")

    cursor.execute("SELECT region, avg(discount_percent) AS dis_percent FROM orders GROUP BY region;")

    table8 = cursor.fetchall()

    answer_8 = pd.DataFrame(table8, columns=['region', 'dis_percent'])

    if st.button("8.Answer"):
        st.dataframe(answer_8)

    st.write("**_9.Find the product category with the highest total profit_**")
    cursor.execute("SELECT category, sum(profit) AS high_profit FROM orders GROUP BY category ORDER BY high_profit DESC;")

    table9 = cursor.fetchall()

    answer_9 = pd.DataFrame(table9, columns=['category', 'high_profit'])

    if st.button("9.Answer"):
        st.dataframe(answer_9)

    st.write("**_10. Calculate the total revenue generated per year_**")

    # Execute the corrected SQL query to group by year
    cursor.execute("SELECT YEAR(order_date) AS revenue_year, SUM(profit) AS revenue_year FROM orders GROUP BY revenue_year ORDER BY revenue_year;")

    # Fetch all results
    table10 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_10 = pd.DataFrame(table10, columns=['revenue_year', 'revenue'])

    # Display the DataFrame
    if st.button("10.Answer"):
        st.dataframe(answer_10)

with col2:
               
       
    st.write("**Analysis 10 Questions Using with Two Table**")
    st.markdown("---")
    st.write("**_11.Top 10 Highest profit in the state_**") 
    cursor.execute("""
             SELECT order1.state, SUM(order2.profit) AS state_profit
             FROM order1
            LEFT JOIN order2 ON order1.order_id = order2.order_id
            GROUP BY order1.state
            ORDER BY state_profit DESC limit 10;
            """)


    table11 = cursor.fetchall()

    #Convert results to a pandas DataFrame with correct column names
    answer_11 = pd.DataFrame(table11, columns=['state', 'profit'])

    # Display the DataFrame
    if st.button("11.Answer"):
        st.dataframe(answer_11)
    
    st.write("**_12.Top 10 Highest quantity sales in the city_**")

    cursor.execute("""
        SELECT order1.city, SUM(order2.quantity) AS city_highest
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
        GROUP BY order1.city
        ORDER BY city_highest DESC limit 10;
        """)
    table12 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_12 = pd.DataFrame(table12, columns=['city', 'quantity'])

    # Display the DataFrame
    if st.button("12.Answer"):
         st.dataframe(answer_12)
    
    st.write("**_13.top 3 Highest profit in ship mode_**")

    cursor.execute("""
        SELECT order1.ship_mode, SUM(order2.profit) AS ship_highest
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
        GROUP BY order1.ship_mode
        ORDER BY ship_highest DESC limit 3;
        """)


    table13 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_13 = pd.DataFrame(table13, columns=['ship_mode', 'profit'])

    # Display the DataFrame
    if st.button("13.Answer"):
         st.dataframe(answer_13)
    
    st.write("**_14.Top 3 list price in the  category_**")

    cursor.execute("""
        SELECT order1.category, SUM(order2.list_price) AS list_highest
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
        GROUP BY order1.category
        ORDER BY list_highest DESC limit 3;
        """)


    table14 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_14 = pd.DataFrame(table14, columns=['category', 'list_price'])

    # Display the DataFrame
    if st.button("14.Answer"):
         st.dataframe(answer_14)

    st.write("**_15.Average discounted price in the  region_**")
    cursor.execute("""
        SELECT order1.region, avg(order2.discounted_price) AS dis_average
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
        GROUP BY order1.region
        ORDER BY dis_average DESC ;
        """)

    table15 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_15 = pd.DataFrame(table15, columns=['region', 'discounted_price'])

    # Display the DataFrame
    if st.button("15.Answer"):
         st.dataframe(answer_15)
    st.write("**_16.Average cost price in the each segment_**")

    cursor.execute("""
        SELECT order1.segment, avg(order2.cost_price) AS segment_average
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
        GROUP BY order1.segment
        ORDER BY segment_average DESC ;
        """)


    table16 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_16 = pd.DataFrame(table16, columns=['segment', 'cost_price'])

    # Display the DataFrame
    if st.button("16.Answer"):
         st.dataframe(answer_16)
    
    st.write("**_17.Top  discount in the category_**")

    cursor.execute("""
        SELECT order1.category, sum(order2.discount) AS discount_highest
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
        GROUP BY order1.category
        ORDER BY discount_highest DESC ;
        """)


    table17 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_17 = pd.DataFrame(table17, columns=['category', 'discount'])

    # Display the DataFrame
    if st.button("17.Answer"):
         st.dataframe(answer_17)
    
    st.write("**_18.10 Highest quantity in the postal code_**")
    cursor.execute("""
        SELECT order1.postal_code, sum(order2.quantity) AS postal_highest
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
        GROUP BY order1.postal_code
        ORDER BY postal_highest DESC limit 10;
        """)


    table18 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_18 = pd.DataFrame(table18, columns=['postal_code', 'quantity'])

    # Display the DataFrame
    if st.button("18.Answer"):
         st.dataframe(answer_18)

    st.write("**_19.Average discount in the state_**")

    cursor.execute("""
        SELECT order1.state, avg(order2.discount) AS discount_average
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
        GROUP BY order1.state
        ORDER BY discount_average DESC limit 10;
        """)


    table19 = cursor.fetchall()

    # Convert results to a pandas DataFrame with correct column names
    answer_19 = pd.DataFrame(table19, columns=['state', 'avgerage_discount'])

    # Display the DataFrame
    if st.button("19.Answer"):
         st.dataframe(answer_19)
    st.write("**_20.Average cost price in the each region_**")

    cursor.execute("""
        SELECT order1.region, avg(order2.cost_price) AS cost_average
        FROM order1
        LEFT JOIN order2 ON order1.order_id = order2.order_id
         GROUP BY order1.region
         ORDER BY cost_average DESC;
        """)


    table20 = cursor.fetchall()
    
    # Convert results to a pandas DataFrame with correct column names
    answer_20 = pd.DataFrame(table20, columns=['region', 'cost_average'])

    # Display the DataFrame
    if st.button("20.Answer"):
         st.dataframe(answer_20)

      
# Closing the connection
cursor.close()
conn.close()




