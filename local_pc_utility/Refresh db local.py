#
# Refresh local database
#
import os, numbers, datetime, subprocess

def main():
    # DB connection
    zip_file_base_name = "db_ejsuser_db_"
    database_name = "ejsuser_db"
    database_user = "root"
    database_pwd = "xxx"
    mysql_exe = "/xampp/mysql/bin/mysql.exe"
    # Dirs
    backup_files_directory = "/users/Richard/Documents/Backup to Livedrive/Latest website backup"; 
    backup_files_directory_alt = "/users/Richard/Latest website backup"; 
    temporary_extract_directory = backup_files_directory + "/restore_temp"

    # Check backup dir exists; if not try to use alternate
    if(not os.path.isdir(backup_files_directory)):
        if(os.path.isdir(backup_files_directory_alt)):
            backup_files_directory = backup_files_directory_alt
        else:
            print("Not readable dir: " + backup_files_directory + " or alternative " + backup_files_directory_alt)
            return
    
    print("Refresh database ")
    
    # Get number of days ago. Default to 1 if empty
    num_days_ago_typed = input("How many days ago was the backup? (1)")
    if(num_days_ago_typed == None):
        num_days_ago_typed = 1 # TODO: Default does not work
    num_days_ago = int(num_days_ago_typed)

    # Get name of zip file
    zip_file_name = get_zip_file_name(zip_file_base_name, num_days_ago)
    zip_file = backup_files_directory + "/" + zip_file_name
    if(not os.path.isfile(zip_file)):
        print("Can't find file: " + zip_file)
        return
    print("Unzipping file " + zip_file)
    
    #extract_zip_file(zip_file, temporary_extract_directory)

    # Load into db
    # Working cmd: /xampp/mysql/bin/mysql.exe -u root -p --password=xxx ejsuser_db < "/users/Richard/Documents/Backup to Livedrive/Latest website backup/db_ejsuser_db_2015_04_17.sql"
    mysql_command = mysql_exe + " -u root -p --password=" + database_pwd + " " + database_name + " < \"" + zip_file + "\" "
    print(mysql_command)
    subprocess.check_call(mysql_command, shell=True)

    print("Database load success")

# Work out zip file name with date
def get_zip_file_name(zip_file_base_name, num_days_ago):
    zip_file_date = datetime.date.today() - datetime.timedelta(days = num_days_ago)
    str_zip_file_date_str = zip_file_date.strftime("%Y_%m_%d")
    zip_file_name = zip_file_base_name + str_zip_file_date_str + ".sql" #Should be ".zip"
    return zip_file_name
    
    
# Run 
main()
