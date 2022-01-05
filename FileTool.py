import csv, json
class FileTool:
    def __init__(self, path, fields):
        self.path = path
        self.fields = fields
        # Let's create our file.
        with open(self.path, 'w', newline='') as outcsv:
            self.headers = self.fields.split(',')
            writer = csv.writer(outcsv)
            writer.writerow(self.headers)

    def menu(self):
        '''
        Main Menu    
        '''
        def search(self):
            '''
            Searches the entered text in the file and prints the line it is in.
            '''
            text = input("Please type the text you want to search: ")
            with open(self.path) as fp:
                for num, line in enumerate(fp, 1):
                    if text in line:
                        print ('Line with text:', num)
                    else:
                        print ('Text not found !')

        def add(self):
            '''
            Appends the entered text to the end of the file
            '''
            text = input("Please type the text you want to add:") # Ex: Furkan,Keskinkilic
            fp = open(self.path, 'a')
            fp.write(text)

        def delete(self):
            '''
            Girilen metnin olduğu satırı siler.
            '''
            text = input("Deletes the line with the entered text:") 
            with open(self.path, "r") as fp:
                lines = fp.readlines()
            with open(self.path, "w") as fp:
                for line in lines:
                    if line.strip("\n") != text:
                        fp.write(line)

        def update(self):
            '''
            Updates the entered line with the entered text
            '''
            text = input("Please type the text you want to update:")
            newtext = input("Please write the text:")
            replacement = ""
            with open(self.path, "r") as fp:        
                for line in fp:
                    line = line.strip()
                    changes = line.replace(text, newtext)
                    replacement = replacement + changes + "\n"
            fp.close()
            
            with open(self.path, "w") as f:
                f.write('\n')
                f.write(replacement)
        def csvToJson(csvfile):
            '''
            Writes the content of the csv file to the json file it creates
            '''
            data = {} 
            with open(csvfile) as f:
                
                if len(self.headers) > 1:
                    reader = csv.DictReader(f)
                    rows = list(reader)
                else:
                    reader = csv.reader(f)
                    i = 1
                    for line in reader:
                        data[i] = line
                        i += 1
            if len(self.headers) > 1:
                with open('output.json', 'w') as o:
                    json.dump(rows, o)
            else:
                with open('output_without_headers.json', 'w') as f:
                    f.write(json.dumps(data))

        def mergeFiles(csvfile):
            '''
            Merges the entered file with the first created file
            '''
            with open(csvfile, 'r') as f1:
                original = f1.read()

            with open(self.path, 'a') as f2:
                f2.write('\n')
                f2.write(original)

        def getHeaders(jsonfile):
            '''
            Prints the header information
            '''
            jsonfile = open(jsonfile, 'r')
            print('Headers: ', jsonfile.readlines(1))

        print("Choose from 1 to 8 \nMenu: ")
        print("1. Search\n2. Add\n3. Delete\n4. Update\n5. Merge files\n6. Converting Csv to Json\n7. Getting headers\n8. Main menu")
        choice = '0'
        while True:
            choice = input ("Your choice: ")
            if choice == "1":
                search(self)
            elif choice == "2":
                add(self)
            elif choice == "3":
                delete(self)
            elif choice == "4":
                update(self)
            elif choice == "5":
                path = input("Enter the new file name: ")
                mergeFiles(path)
            elif choice == "6":
                path = input("Enter the file name: ")
                csvToJson(path)
            elif choice == "7":
                path = input("Enter the file name: ")
                getHeaders(path)
            elif choice == "8":
                self.menu()
            else:
                print("Wrong choice !")


fileName = input('Enter filename:') # Ex: sample.csv
fields  = input('Enter Headers:') # Ex: Name,Surname

FileTool(fileName, fields).menu()