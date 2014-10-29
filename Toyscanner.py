import sys
global charClass,nextChar,nextToken,lexeme;
global EOF,LETTER,DIGIT,UNKNOWN,INT_LIT,IDENT,ASSIGN_OP,ADD_OP,SUB_OP,MULT_OP,DIV_OP,LEFT_PAREN,RIGHT_PAREN;
global in_fp;
charClass="";
nextChar="";
lexeme="";
nextToken=0
EOF=-1
LETTER=0
DIGIT=1
UNKNOWN=99
INT_LIT=10
IDENT=11
ASSIGN_OP=20
ADD_OP=21
SUB_OP=22
MULT_OP=23
DIV_OP=24
LEFT_PAREN=25
RIGHT_PAREN=26

def getChar():
        global nextChar,charClass;
        nextChar=in_fp.read(1);
        getNonBlank();
        if nextChar !="":
            if nextChar.isalpha():
               charClass = LETTER;
            elif nextChar.isdigit():
               charClass = DIGIT;
            else:
               charClass = UNKNOWN;
        
def addChar():
        global lexeme,nextChar;
        lexeme=lexeme + nextChar;
                    
def getNonBlank():
        global nextChar
        while nextChar.isspace():
            getChar();

def  lex():
        global lexeme,charClass,nextToken,nextChar;
        lexeme="";
        
        if (charClass==LETTER):
            addChar()
            getChar()
            while(charClass==LETTER)or(charClass==DIGIT):
                if nextChar == "":
                    charClass = EOF;
                    break;
                addChar()
                getChar()
            nextToken=IDENT;
           
        elif (charClass == DIGIT):
            addChar()
            getChar()
            while (charClass == DIGIT):
                addChar()
                getChar()
            nextToken=INT_LIT; 
           
        elif (charClass == UNKNOWN):
            lookup(nextChar);
            getChar()
           
        elif charClass == EOF:
            nextToken=EOF
            lexeme="EOF";
           
        print "Next Token:",nextToken, "Next Lexeme:",lexeme;
             
        
def lookup(ch):
        global nextToken,lexeme;
        if(ch=='('):
            addChar()
            nextToken=LEFT_PAREN;
        
        elif(ch==')'):
            addChar()
            nextToken=RIGHT_PAREN;
        
        elif(ch=='+'):
            addChar()
            nextToken=ADD_OP;
        
        elif(ch=='-'):
            addChar()
            nextToken=SUB_OP;

        elif(ch=='*'):
            addChar()
            nextToken=MUL_OP;

        elif(ch=='/'):
            addChar()
            nextToken=DIV_OP;

        else:
            addChar()
            nextToken=EOF;
            lexeme="EOF";
            
if __name__ == '__main__':
    global in_fp
    parse=0
    try:
        if len(sys.argv)==2:
            in_fp = open(sys.argv[1],'r')
            parse=1
        elif(len(sys.argv))==1:
            in_fp=open('front.in','r')
            parse=1
        else :
            print 'Usage:\n Python input.txt[file-to-parse(optional,default=input.txt)]'
    except :
        print "expected error:",sys.exc_info()[0]
        raise
    if parse:
        getChar();
        lex();
        while (nextToken!=EOF):
          lex();
        in_fp.close();

            

    

    
           
            
            
    
  
        
       
    
    
        
    
    

    
