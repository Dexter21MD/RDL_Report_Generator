

# Class for holding global namespaces
class Global_Rdl_namespaces():
    def __init__(self):
        self.rb_v15_ns_dict = {
            'default:': 'http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition',
            'rd:': 'http://schemas.microsoft.com/SQLServer/reporting/reportdesigner',
            'df:': 'http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition/defaultfontfamily'
        }

    def get_namesoaces_for_reportbuilder(self, rb_version="v15"):
        match rb_version:
            case "v15":
                return self.rb_v15_ns_dict
            case _:
                return {}
