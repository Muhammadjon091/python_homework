pip install pandas sqlite3


import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect('chinook.db')


# Query to calculate total amount spent by each customer
query_total_spent = '''
SELECT
    c.CustomerId,
    c.FirstName || ' ' || c.LastName AS CustomerName,
    SUM(i.Total) AS TotalSpent
FROM
    Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY
    c.CustomerId
ORDER BY
    TotalSpent DESC;
'''

# Execute the query and load into a DataFrame
df_total_spent = pd.read_sql_query(query_total_spent, conn)



# Get the top 5 customers
top_5_customers = df_total_spent.head(5)
print(top_5_customers)




# Query to determine if a purchase is for a whole album or individual tracks
query_purchase_type = '''
WITH AlbumTracks AS (
    SELECT
        alb.AlbumId,
        COUNT(tr.TrackId) AS TotalAlbumTracks
    FROM
        Album alb
        JOIN Track tr ON alb.AlbumId = tr.AlbumId
    GROUP BY
        alb.AlbumId
),
InvoiceAlbumPurchases AS (
    SELECT
        il.InvoiceId,
        MIN(albtrk.TotalAlbumTracks) AS AlbumTrackCount,
        COUNT(il.TrackId) AS PurchasedTrackCount,
        CASE
            WHEN COUNT(il.TrackId) = MIN(albtrk.TotalAlbumTracks) THEN 'Album'
            ELSE 'Individual'
        END AS PurchaseType
    FROM
        InvoiceLine il
        JOIN Track tr ON il.TrackId = tr.TrackId
        JOIN AlbumTracks albtrk ON tr.AlbumId = albtrk.AlbumId
    GROUP BY
        il.InvoiceId
)
SELECT
    PurchaseType,
    COUNT(*) AS NumberOfPurchases
FROM
    InvoiceAlbumPurchases
GROUP BY
    PurchaseType;
'''

# Execute the query and load into a DataFrame
df_purchase_type = pd.read_sql_query(query_purchase_type, conn)



# Calculate total number of purchases
total_purchases = df_purchase_type['NumberOfPurchases'].sum()

# Calculate percentage for each purchase type
df_purchase_type['Percentage'] = (df_purchase_type['NumberOfPurchases'] / total_purchases) * 100

print(df_purchase_type)




vc# Close the connection
conn.close()

