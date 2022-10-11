import sys

def main():
    if (len(sys.argv) >= 3):
        files = []
        for i in range(1, len(sys.argv)):
            filePath = sys.argv[i]
            files.append(filePath)
            
            # Check if file is of type .csv
            fileName = ""
            for i in range(len(filePath) - 1, -1, -1):
                if filePath[i] == '/':
                    break
                fileName = filePath[i] + fileName
            if fileName[len(fileName) - 4: len(fileName)] != ".csv":
                raise TypeError("Make sure the provided files are of type .csv")

        columns = []
        try:
            inFile = open(files[0], "r")
            line = inFile.readline()
            columns = line.split(',')
            inFile.close()
        except IOError:
            print("File not found")
            sys.exit(1)

        # Check all csv files have matching columns
        for f in files:
            try:
                inFile = open(f, "r")
                line = inFile.readline()
                if columns != line.split(','):
                    raise ValueError("Make sure all .csv files have the same columns")
                inFile.close()
            except IOError:
                print("File not found")
                sys.exit(1)

        # Output columns for combined.csv
        output = ""
        for col in columns:
            output = output + col + ','
        # Strip extra , and \n
        output = output[0: len(output) - 2]
        output += ",filename"
        print(output)

        # Output lines for combined.csv
        for f in files:
            # Get file name
            fileName = ""
            for i in range(len(f) - 1, -1, -1):
                if f[i] == '/':
                    break
                fileName = f[i] + fileName
            # Print lines in files
            try:
                inFile = open(f, "r")
                for line in inFile:
                    if line.split(',') != columns:
                        output = line + ','
                        output = output[0: len(output) - 2]
                        output = output + ',' + fileName
                        print(output)
            except IOError:
                print("File not found")
                sys.exit(1)
    else:
        raise SyntaxError("Please provide a minimum of 2 csv files.")

if __name__ == "__main__":
    main()
