import os
import fileinput, sys
import in_place
import codecs
import getpass

#events_folder = r'C:\Users\\' + str(username) + r'\Documents\Paradox Interactive\Hearts of Iron IV\mod\EoaNB2\EoaNB\toi\events'
scripted_loc_folder = r'C:\Users\\' + getpass.getuser() + r'\Documents\Paradox Interactive\Hearts of Iron IV\mod\EoaNB2\EoaNB\toi\common\scripted_localisation'
output_file_path = r'C:\Users\\' + getpass.getuser() + r'\Documents\Paradox Interactive\Hearts of Iron IV\mod\EoaNB2\EoaNB\toi\localisation\english\scripted_loc_replace.txt'
current_line = " "
current_loc_string = " "
current_loc_key = " "
#string_addition = "\n\nimmediate = {\n\tlog = \"[THIS.GetTag]: firing " + str(current_event) + "\"\n}"
#name_check = ' '
loc_name = ' '
new_loc_line = ' '
new_loc_string = ' '
#pictureVar = 'picture'
destination_file_path = r'C:\Users\\' + getpass.getuser() + r'\Documents\Paradox Interactive\Hearts of Iron IV\mod\EoaNB2\EoaNB\toi\localisation\english\scripted_loc_replace.txt'

with open(destination_file_path, "w") as file_out:
    for file in os.listdir(scripted_loc_folder):
        current_line = '\n\n\n# start of file '
        current_line = current_line + file
        file_out.write(current_line + "\n")
        file_path = os.path.join(scripted_loc_folder, file)
        with in_place.InPlace(file_path) as file_read:
                for line in file_read:
                    if 'localization_key = \"' in line:
                        print('loc spotted')
                        print(line)
                        if (line.find('#') > -1)&(line.find('#') < line.find("localization_key")):
                            file_read.write(line)
                            continue
                        if line.find('\"GFX_') > 0:
                            file_read.write(line)
                            continue
                        #getting localization string  ##################  
                        current_line = line
                        current_line = current_line[0:(current_line.rfind('\"'))]
                        current_line = current_line[(current_line.find('\"') + 1):]
                        current_loc_string = current_line #saves old localization string##############
                        print('current_loc_string is ' + current_line)
                        #formatting loc to get new key##############
                        current_loc_key = current_line
                        current_loc_key = current_loc_key.replace("[", "LBracketSym_")
                        current_loc_key = current_loc_key.replace("]", "RBracketSym_")
                        current_loc_key = current_loc_key.replace("?", "QuestionMark_")
                        current_loc_key = current_loc_key.replace(".", "PeriodMark_")
                        current_loc_key = current_loc_key.replace(",", "CommaMark_")
                        current_loc_key = current_loc_key.replace("|", "ORSym_")
                        current_loc_key = current_loc_key.replace(":", "ColonSym_")
                        current_loc_key = current_loc_key.replace("@", "AtSym_")
                        current_loc_key = current_loc_key.replace("^", "CaratSym_")
                        current_loc_key = current_loc_key.replace("+", "PlusSign_")
                        current_loc_key = current_loc_key.replace("=", "EqualsSign_")
                        current_loc_key = current_loc_key.replace("%", "PercentSym_")
                        current_loc_key = current_loc_key.replace("$", "DollarSign_")
                        current_loc_key = current_loc_key.replace("(", "LParenthesi_")
                        current_loc_key = current_loc_key.replace(")", "RParenthesi_")
                        current_loc_key = current_loc_key.replace(" ", "_")
                        current_loc_key = current_loc_key.replace("\"", "QuotationMark_")
                        current_loc_key = "scripted_loc_" + current_loc_key
                        #current_loc_key = current_loc_key[0:(current_loc_key.rfind('_'))]
                        if current_loc_key[((len(current_loc_key)-1))] == '_':
                            current_loc_key = current_loc_key[:-1]
                        print("current_loc_key is " + current_loc_key)

                        #pasting new key in scripted loc file###############
                        new_loc_line = line
                        new_loc_line = new_loc_line[:(new_loc_line.index('\"'))]
                        new_loc_line = new_loc_line + current_loc_key + '\n'
                        new_loc_line = new_loc_line.strip('[')
                        new_loc_line = new_loc_line.strip(']')
                        new_loc_line = new_loc_line.strip('?')
                        new_loc_line = new_loc_line.strip('.')
                        new_loc_line = new_loc_line.strip('|')
                        new_loc_line = new_loc_line.strip(':')
                        new_loc_line = new_loc_line.strip('@')
                        new_loc_line = new_loc_line.strip('^')
                        new_loc_line = new_loc_line.strip('+')
                        new_loc_line = new_loc_line.strip('=')
                        new_loc_line = new_loc_line.strip('%')
                        new_loc_line = new_loc_line.strip('$')
                        new_loc_line = new_loc_line.replace(' ', '_')
                        new_loc_line = new_loc_line.replace(':', '_')
                        new_loc_line = new_loc_line.strip('\"')
                        new_loc_line = new_loc_line.replace('localization_key_=_', 'localization_key = ')
                        print("midway new_loc_line is " + new_loc_line)
                        for i in range(len(new_loc_line)):
                            if ((new_loc_line[i] == ' ')|(new_loc_line[i] == '_')) & (i < new_loc_line.find('localization_key')):
                                print("character at i is " + new_loc_line[i])
                                new_loc_line = list(new_loc_line)
                                new_loc_line[i] = " "
                                new_loc_line = "".join(new_loc_line)
                            #elif (new_loc_line[i] == '"'):
                                #new_loc_line[i] = ''
                        print('new_loc_line is ' + new_loc_line)
                        file_read.write(new_loc_line)

                        #pasting old loc and new key in localization file########
                        new_loc_string = current_loc_key
                        new_loc_string = new_loc_string + ': \"'
                        new_loc_string = new_loc_string + current_loc_string
                        new_loc_string = new_loc_string + '\"\n'
                        print('new_loc_string is ' + new_loc_string)
                        file_out.write(new_loc_string)
                        continue

                    else:
                        #print('exception e')
                        file_read.write(line)
