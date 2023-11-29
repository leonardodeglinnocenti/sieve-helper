

class SieveUtilities():

    def generate_sieve_config(config):
        # config has shape [email, from_check, to_check, target_folder]
        out_string = "require \"fileinto\";"
        first_iter = True
        for c in config:
            email = c[0]
            from_check = c[1]
            to_check = c[2]
            target_folder = c[3]

            out_string += "\n"

            if from_check and to_check:
                if first_iter:
                    out_string += "if address :is [\"From\", \"To\"] \""
                else:
                    out_string += "elsif address :is [\"From\", \"To\"] \""
            elif from_check and not to_check:
                if first_iter:
                    out_string += "if address :is [\"From\"] \""
                else:
                    out_string += "elsif address :is [\"From\"] \""
            else:
                if first_iter:
                    out_string += "if address :is [\"To\"] \""
                else:
                    out_string += "elsif address :is [\"To\"] \""

            if first_iter:
                first_iter = False

            out_string += email
            out_string += "\"{\n {fileinto \""
            out_string += target_folder
            out_string += "\";\n}"

        return out_string


