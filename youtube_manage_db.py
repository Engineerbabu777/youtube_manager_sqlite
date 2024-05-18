import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
        ''')



def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name,time))
    conn.commit()
    
def update_video(vid,name,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(name,time,vid))
    conn.commit()


def delete_video(vid):
    cursor.execute("DELETE FROM videos WHERE id = ?",(vid,))
    conn.commit()

def main():
    while True:
        print("Youtube Manage App | DB Sqlite3")
        print("\n1- List Videos.\n")
        print("2- Add Videos.\n")
        print("3- Update Videos.\n")
        print("4- Delete Videos.\n")
        print("5- Exit :) \n")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
        elif choice == "2":
         name = input("Enter your name: ")
         time = input("Enter your time: ")
         add_video(name,time)
        elif choice == "3":
         video_id = input("Enter video id: ")
         name = input("Enter your name: ")
         time = input("Enter your time: ")
         update_video(video_id,name,time)
        elif choice == "4":
         video_id = input("Enter video id: ")
         delete_video(video_id)
        else:
         break     
          
          
    conn.close()  
            
        
        



if __name__ == "__main__":
    main()