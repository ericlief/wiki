# -*- coding: utf-8 -*-

import regex as re    

#tokenize_func (function, optional) – Function that will be used for tokenization. By default, use tokenize(). 
#If you inject your own tokenizer, it must conform to this interface: 
#tokenize_func(text: str, token_min_len: int, token_max_len: int, lower: bool) -> list of strdef tokenize(text):
    
def tokenize(text, token_min_len=1, token_max_len=50, lower=False):
    """
    Tokenize the given sentence in Portuguese.
    :param text: text to be tokenized, as a string
    :param token_min_len: int
    :param token_max_len: int
    :param lower: lowercase, bool)
    
    """
    abbrev_fh = 'abbreviations_pt.py'
        

    # Read abbrev list and build regex for these
    abbrev = ""    
    try:
        with open(abbrev_fh, 'r') as f:
            print('getting abrev')
            for line in f:
                #print(line)
                pre = line.strip()
                if pre and pre[0] != '#':
                    #print(pre)
                    pre = re.escape(pre, special_only=True, literal_spaces=True)
                    #print(pre)
                    abbrev += pre + '|'
                    
    except IOError:
        print('Abbreviation file not found')
    
    #abbrev = abbrev[:-2]
    #print(abbrev)
    #p1 = re.compile(r'[.,!]')
    #p1.sub(' \1 ', text)
    ##text = re.sub('[.,!]', ' \1 ', text)
    
    ## Deal with special symbols
    ##re.sub(text, 
    
    #print(repr(text))
    
    # Turn ` into '
    #$text =~ s/\`/\'/g;
    text = re.sub('`', "'", text)
    
    #turn '' into "
    #$text =~ s/\'\'/ \" /g;    
    text = re.sub("''", '"', text)
    
    # Get rid of extraneous spaces
    text = re.sub(" {2,}", " ", text)
    
    #regex = r'''%s'''%abbrev
    #regex = "\d+(?:[,\.]\d+)*"
    #'''.format(abbrev) # % abbrev
    
    regex = r"""(?uxi) # Flags: UNICODE, VERBOSE, IGNORECASE
    
    # Numbers
    #(?:\(?\+?\d{1,3}\)?)?\s*(?:\d+[\.\s-]?)+\d+|
    #(?:\(?\+?\d{1,3}\)? )?\d+(?:[,\. -]\d+)*|
    (?:\(?\+?\d{1,3}\)?[ ]*)?\d+(?:[:\/,\. -]\d+)*|  
    
    
    # Numbers in format 999.999.999,999, and (216) 729-9295, 4:15
    # possibly followed by hyphen and alphanumerics, \B- avoids A-1.1-a-a producing a negative number
    #(?:\B-)?\d+(?:[,\.]\d+)*(?:-?\w)*| 
    #\d+(?:[,\.]\d+)*| 
    
    
    # One letter abbreviations, e.g. E.U.A.  
    (?:\w\.)+| 
    
    # Abbreviations/Nonbreaking prefixes from list
    #(?:\b # doesn't seem to work a/c/ -> a/c /, on one line throws error for extra )
    %s
    #\b)
    #|

    # Emails
    #(?:[a-z0-9!#$%%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%%\&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])|
    
    # URLs
    #(?:https?://)?\w{2,}(?:\.\w{2,})+(?:/\w+)*|   
    
    # Hashtags and twitter names
    #(?:[\#@]\w+)| 
      
    ## Phone numbers
    ##(?:\(?\+?\d{1,3}\)?)?\s*(?:\d+[\.\s-]?)+\d+|

    # Ellipsis or sequences of dots
    \.{3,}|                           

    # Alphanumerics
    \w+|                              

    # Any sequence of dashes 
    -+|

    # Any non-space character
    \S  
    
    """ % abbrev
    
    #print(regex[3256:3270])
    #print(repr(regex))
    
    #print('a/c in string:', re.findall('a/c',regex))
    
    #p = re.compile(regex, flags=re.UNICODE|re.VERBOSE|re.IGNORECASE)
    #return p.findall(text, re.UNICODE|re.VERBOSE|re.IGNORECASE)
    p = re.compile(regex)
    return p.findall(text)

    #regex = r'%s'%abbrev
    #print(regex)
    #print(re.escape(regex, special_only=True))
    
 
    #regex = r'''(?ux)
    #%s
    ##\w+
     ### the order of the patterns is important!!
     ### more structured patterns come first
     ##[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+|    # emails
     ##(?:https?://)?\w{2,}(?:\.\w{2,})+(?:/\w+)*|                  # URLs
     ##(?:[\#@]\w+)|                     # Hashtags and twitter user names
     ##(?:[^\W\d_]\.)+|                  # one letter abbreviations, e.g. E.U.A.
     ##(?:[DSds][Rr][Aa]?)\.|            # common abbreviations such as dr., sr., sra., dra.
     ##(?:\B-)?\d+(?:[:.,]\d+)*(?:-?\w)*|
         ### numbers in format 999.999.999,999, possibly followed by hyphen and alphanumerics
         ### \B- avoids picks as F-14 as a negative number
     ##\.{3,}|                           # ellipsis or sequences of dots
     ##\w+|                              # alphanumerics
     ##-+|                               # any sequence of dashes
     ##\S                                # any non-space character
     ##''' #% abbrev
 
 
    
    #tokenize = RegexpTokenizer(tokenize_regexp)
    
    #print(re.findall(regex, text, re.VERBOSE, re.IGNORECASE))
    #print(re.findall(regex, text))
    #print(p.findall(text))
    
    #print(re.split(regex, text))

 
#while True:
    #s = input("enter regex")
    #tokenize(s)    

if __name__ == "__main__":

    import lzma
    
    s = r"E.U.A., Il.mo  a/c a/c/ c/ ele. pág. 2, sec. 2.3.1 Sup... 12:12:23 12/2/2012 \'\`  10,10,10 33-33-33 100.0.1,33 ''Dr. Erique A. Lief, Ph.D'', dra. Rocha, il.mo sr. Moraes. telefone +420 77.655.65.49 +420 77 655 65 49 e ele... a/c Ilma./ilma./il.ma/Ilma N.Sra. Garcia' . esse grande cabrão!--que é Dra. Morções; seu João às costas! 10,00.34, '4:15 p.m.' eric23_lief28@seznam.cz"

    
    print(tokenize(s))
    
    #in_fh = '/data/pt.deduped.xz'
    #out_fh = 'out-pt.txt'
    #with open(out_fh, 'wt') as out:
        #with lzma.open(in_fh, 'rt') as f:
            #for line in f:
                #tokens = tokenize(line)
                #if tokens:
                    #sent = " ".join(tokens)
                    #print(sent)