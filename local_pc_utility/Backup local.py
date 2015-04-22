#
# Backup local directories
#

import sys,os,shutil,datetime

def main():

    # Setup vars
    dirs_to_backup = [
         "Y:/Berners Green",
         "Y:/Rachel doc",
         "Y:/Richard doc",
         "Z:/backup_data_and_ini_files",
         "C:/Users/Richard/Dropbox/EuroJobsites",
         "C:/Users/Richard/Dropbox/KP",

         # Occasional backup
         #"Z:/EuroJobsites pics",

         # Unused??
         #"C:/Users/Richard/Google Drive", #Not sure these are real docs
         #"Z:/Tech Notes RF"
    ]
    backup_store_dir = "C:/Users/Richard/Documents/Backup to Livedrive/Current Backups/"
    #backup_store_dir = "C:/Users/Richard/Documents/Temp/Backup test"
    
    print("Running regular backup");
    print("Backups will be written to " + backup_store_dir)
    start_time = datetime.datetime.now().time()
    print_with_time("Started")

    for dir_to_backup in dirs_to_backup:
        zip_and_move_to_store_dir( dir_to_backup, backup_store_dir )

    print_with_time("Finished")
    print("NOW Export Google Docs")
    input("Hit return to exit")

# Zip file and move to store dir
def zip_and_move_to_store_dir( dir_to_zip, backup_store_dir ):
    
    print_with_time("Backing up " + dir_to_zip + "...")
    
    # Check arguments are valid dirs
    if(not os.path.isdir(dir_to_zip)):
        raise ValueError("Not a readable dir: " + dir_to_zip)
    if(not os.path.isdir(backup_store_dir)):
        raise ValueError("Not a writeable dir: " + backup_store_dir)

    # Create archive file name
    current_date_string = str(datetime.date.today())
    base_name = backup_store_dir + "/" + os.path.basename(dir_to_zip) + "." + current_date_string
    
    # If zip file exists already, remove it
    zip_file = base_name + ".zip"
    if(os.path.isfile(zip_file)):
       os.remove(zip_file)
       print("Archive already exists: Removing " + zip_file)

    # Create zip file
    archive_name = shutil.make_archive(base_name, "zip", dir_to_zip )
    print_with_time("Created archive " + archive_name)

# Print with time
def print_with_time(msg):
    print( datetime.datetime.now().time().strftime("%H:%M:%S ") + msg )

#Run main()
main()  
