#display
import sqlite3

def main():
	con = sqlite3.connect(r"C:/Users/yenap/Desktop/pitchfork-reviews.db")
	sql = con.cursor()
	sql.execute("""SELECT * from albums""")
	rows = sql.fetchall()
	for row in rows:
		print(row[1] + ' | ' + row[2] + ' | ' + str(row[3]))

if __name__ == "__main__":
	main()