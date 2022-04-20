class Table:
    # Default values to indicate error/initialize w/ no label
    data = [ ["Something went wrong."] ]
    label = ""
    width = 80
    
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = 1

        # Find largest row to assign col count
        for row in data:
            i = len(row)
            if i > self.cols:
                self.cols = i

        # Declare/Initialize miscellaneous values used throughout
        self.col_width = int(self.width / self.cols) - 1
        self.table_width = self.width - self.width % self.col_width

    # Method for user to add a label/title to the table
    def addLabel(self, label):
        self.label = label

    # Method for user to set width manually
    def setWidth(self, width):
        self.width = width
        self.col_width = int(self.width / self.cols) - 1
        self.table_width = self.width - self.width % self.col_width

    # Creates the horizontal dividers of the table, with or without the label
    def makeSeparator(self, label):
        result = ""
        iterable = range(self.table_width)

        if label:
            result += "+" + self.label
            iterable = range(len(self.label) + 1, self.table_width)

        for i in iterable:
            if i % self.col_width != 0:
                result += "-"
            else:
                result += "+"
        return result + "+\n"

    # Truncates long strings and formats a row into multple lines that fit within the table
    def makeRow(self, data):
        cutoff = self.col_width - 4 # The # of available characters in 1 line of a cell

        # Checks if any strings in the last row are above truncation length
        for string in data[len(data) - 1]:

            # If any are, create 2 new arrays, one to replace the current row and another for the next
            if len(string) > cutoff:
                replacerRow = []
                nextRow = []

                for string in data[len(data) - 1]:
                    # If a word gets cut off, add a hyphen
                    line = string[:cutoff]
                    if len(line) >= cutoff and string[len(line)] != " ":
                        line += "-"
                    # If a line ends in " -", clip it
                        # This happens because a word can get cut off at the first letter
                        # This doesn't give enough space fo the first char and hyphen
                    if line[-2:] == " -":
                        line = line[:-2]
                    
                    # Append substrings to appropriate arrays
                    replacerRow.append(line)
                    nextRow.append(string[cutoff:].strip())
                
                # Place arrays into data
                data[len(data) - 1] = replacerRow
                data.append(nextRow)

                # Recurse and check the new row for long strings
                return self.makeRow(data)

        # If none, return the truncated data
        return data
        
    # Main method-- returns a printable ascii table string
    def toString(self):
        result = self.makeSeparator(True) # Make the first divider with a label

        for row in self.data:
            # Clean up any ragged arrays
            if len(row) < self.cols:
                for i in range(self.cols - len(row)):
                    row.append("")
            rowData = self.makeRow([ row ]) # Sets up rowData as 2d array

            # For each line in the returned rowData, format to fit the table w/ proper spacing
            for line in rowData:
                appendString = "|"
                for string in line:
                    appendString += " {}{}".format(string, " " * (self.col_width - 2 - len(string)))
                    appendString += "|"
                result += appendString.strip() + "\n"
            
            # Add the divider between rows
            result += self.makeSeparator(False)
            
        return result