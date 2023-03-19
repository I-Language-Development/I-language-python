
class LexerToken:
    def __init__(self,typ,val):
        self.type = typ
        self.value = val
    def __str__(self):
        return "{" + self.type + ":'" + self.value + "'}"

    def __repr__(self):
        return "{" + self.type + ":'" + self.value + "'}"

class LexerError(BaseException):
    def __init__(self,description,line,column):
        self.desc = description
        self.line = line
        self.column = column
    def __str__(self):
        return str(self.desc) + " in line " + str(self.line) + ", column " + str(self.column)

class Lexer:
    def __init__(self,text):
        self.text = text
        self.separators = [" ","\t","\n"]
        self.doublemarks = {"==":"EQUAL","++":"COUNT_UP",">=":"GREATER_EQUAL","<=":"LESS_EQUAL",\
        "&&":"AND","!=":"NOT_EQUAL","||":"OR"}
        self.marks = {';':"END_CMD","=":"SET","{":"BLOCK_OPEN","}":"BLOCK_CLOSE",\
            "(":"BRACKET_OPEN",")":"BRACKET_CLOSE",\
            "[":"INDEX_OPEN","]":"INDEX_CLOSE",\
            "?":"INDEFINITE",\
            ".":"SEPERATOR",\
            ":":"SLICE",\
            ">":"GREATER",\
            "<":"LESS","!":"NOT",
            "+":"ADD","-":"SUBTRACT","*":"MULTIPLY","/":"DIVIDE"}
        self.keywords = {"class":"CLASS","use":"USE","import":"IMPORT",\
            "if":"IF","else":"ELSE","while":"WHILE","for":"FOR","return":"RETURN","delete":"DELETE"}
        self.basetypes = ["string","int","float","bool","dynamic"]
        
        self.tokens = []
        
    def lex(self):
        def validFLOAT(string):
            dot = False
            valid = True
            if string[0] == "-": string = string[1:]
            for char in string:
                valid = valid and (char in ["0","1","2","3","4","5","6","7","8","9"] or (char == "." and dot == False))
                if char == ".": dot = True
            return valid
        def validINT(string):
            valid = True
            if string[0] == "-": string = string[1:]
            for char in string:
                valid = valid and char in ["0","1","2","3","4","5","6","7","8","9"]
                
            return valid
        
        def gettoken(string,l,c):
            if string in list(self.keywords.keys()):
                return LexerToken(self.keywords[string],string)
            elif len(string) > 0 and string[0] == "_":
                return LexerToken("BUILTIN_CONST",string)
            elif string == "true" or string == "false":
                return LexerToken("BOOL",string)
            elif string in self.basetypes:
                return LexerToken("BASETYPE",string)
            elif len(string) == 0:
                return None
            elif validFLOAT(string):
                if validINT(string): return LexerToken("INT",string)
                return LexerToken("FLOAT",string)
            
            elif len(string) > 0 and string[0] not in ["0","1","2","3","4","5","6","7","8","9"]:
                return LexerToken("NAME",string)
            
            else:
                raise LexerError("Unrecognized Pattern: '" + string + "'",l,c)
        def repl(ar):
            n = []
            for el in ar:
                if el is not None:
                    n.append(el)
            return n
        line = 1
        comment = 0
        column = 1
        index = 0
        buffer = ""
        instring = False
        while index < len(self.text):
            if self.text[index] == "\n":
                self.tokens.append(gettoken(buffer,line,column))
                line += 1
                column = 1
                buffer = ""
                if comment == 1: comment = 0
            else: column += 1
            if comment < 1:
                
                if (len(self.text[index:])>1 and self.text[index:index+2]=="//"):
                    comment = 1
                elif self.text[index] == "'" or self.text[index] == "\"":
                    instring = not instring
                    if not instring:
                        self.tokens.append(LexerToken("STRING",buffer))
                        
                        buffer = ""
                    
                elif instring:
                    buffer += self.text[index]
                elif self.text[index] in self.separators:
                    self.tokens.append(gettoken(buffer,line,column))
                    buffer = ""
                elif len(self.text[index:])>1 and self.text[index:index+2] in list(self.doublemarks.keys()):
                    self.tokens.append(gettoken(buffer,line,column))
                    self.tokens.append(LexerToken(self.doublemarks[self.text[index:index+2]],self.text[index:index+2]))
                    buffer = ""
                    index += 1
                    
                elif self.text[index] in list(self.marks.keys()):
                    self.tokens.append(gettoken(buffer,line,column))
                    self.tokens.append(LexerToken(self.marks[self.text[index]],self.text[index]))
                    buffer = ""
                
                else:
                    buffer += self.text[index]
            
            index += 1
        self.tokens = repl(self.tokens)
        return self.tokens
        
if __name__ == "__main__":
    f = open("arraysfile.il")
    d = f.read()
    f.close()
    l = Lexer(d)
    print(l.lex())

