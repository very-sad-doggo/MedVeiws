import pandas as pd
import psycopg2
from psycopg2 import Error

from WebApp.models import ConnectingToKIS
from . import string_snippets


class Queries:
    """ This object consists of gotten values from web pages
     and returns full query in string format ready to use in DB. """
    types_converting = {
        'Лабораторные исследования': 1,
        'Инструментальные исследования': 2,
        'Процедуры и манипуляции': 3,
        'Операции': 4,
        'Консультации': 5
    }

    def __init__(self, dept, research, from_dt, to_dt):
        self.dept = dept
        self.research = research
        self.from_dt = from_dt
        self.to_dt = to_dt

    def ready_select(self):
        return f'SELECT' \
               f' concat_ws (\' \',p.surname,p.name,p.patron) AS Назначил,' \
               f' concat_ws (\' \',m.num,m.YEAR) AS №ИБ,' \
               f' concat_ws(\' \',m.surname,m.name,m.patron) AS ФИО_Пациента,' \
               f' n.name AS Назначение,' \
               f' to_char(n.create_dt, \'DD.MM.YYYY HH:MM\') AS Создано,' \
               f' to_char(n.plan_dt, \'MM.YYYY HH:MM\'),' \
               f' CASE n.naz_extr_id ' \
               f'\tWHEN \'0\' THEN \'Планово\' ' \
               f'\tWHEN \'1\' THEN \'Экстренно\' ' \
               f' ELSE n.naz_extr_id::TEXT ' \
               f' END ' \
               f' FROM mm.mdoc AS m ' \
               f' JOIN mm.hospdoc h ON h.mdoc_id = m.id ' \
               f' JOIN mm.naz n ON n.mdoc_id = m.id ' \
               f' JOIN mm.emp AS em ON  em.id = n.creator_emp_id ' \
               f' JOIN mm.dept AS dp ON  dp.id = em.dept_id ' \
               f' JOIN mm.people AS p ON  p.id = em.people_id ' \
               f' JOIN mm.ehr_case ec ON ec.id = h.ehr_case_id ' \
               f' LEFT JOIN mm.naz_action na  ON na.id = n.id ' \
               f' WHERE n.create_dt BETWEEN \'{self.from_dt}\' AND \'{self.to_dt}\' ' \
               f' AND n.naz_view = \'{self.types_converting[self.research]}\'' \
               f' AND n.naz_state_id = 2 ' \
               f' AND dp.name = \'{self.dept}\''


class SelectAnswer:
    """ Represent SQL query object in the text format. """
    def __init__(self, query_text):
        self.query_text = query_text

    def selecting(self):
        """ Connecting to DB and execute SQL query. If connect not established or
        bad query getting - throw exceptions that displaying on the web page. """
        if len(ConnectingToKIS.objects.all()) != 0:
            for conn_data in ConnectingToKIS.objects.all():
                if conn_data.active is True:
                    try:
                        connection = psycopg2.connect(database=conn_data.db,
                                                      host=conn_data.host,
                                                      #port =5431,
                                                      port=conn_data.port,
                                                      user=conn_data.user,
                                                      password=conn_data.password)
                        try:
                            cursor = connection.cursor()
                            cursor.execute(self.query_text)
                            selecting_data = cursor.fetchall()
                            return selecting_data
                        except (Exception, Error) as e:
                            return f'Error!\n\n{e}\n'
                        finally:
                            cursor.close()
                            connection.close()
                    except (Exception, Error) as e:
                        return f'Error!\n\n{e}\n'
                else:
                    return 'DB not active!\n To use it - turn on check box in the admin panel!'
        else:
            return 'There are no any records in the BD data tab!'


class ReadyReportHTML:
    """ Represent HTML page and contains selected required data.
    The data converts to HTML code by Pandas DataFrame. Data for connecting get from app DB models. """
    top_of_template = string_snippets.top_of_template
    bot_of_template = string_snippets.bot_of_template

    def __init__(self, db_data):
        self.db_data = db_data

    def output_data(self):
        """ Prepare raw data getting from KIS DB and creating HTML template based on them. Data handled by PANDAS. """
        if type(self.db_data) is list and len(self.db_data) == 0:
            tab = string_snippets.tab_done
        elif type(self.db_data) is list and len(self.db_data) != 0:
            row_values = len(self.db_data[0])
            rows_number = len(self.db_data)
            headers_names = ['Назначил', 'Номер ИБ', 'Пациент', 'Назначение',
                             'Дата создания', 'Назначено на дату', 'Статус']
            # List of lists of data separated and grouped inside
            data_lists = [list(map(lambda x: x[i], self.db_data)) for i in range(row_values)]
            # Creating dict for DataFrame
            data = dict(zip(headers_names, data_lists))
            df = pd.DataFrame(data=data, index=range(1, rows_number+1))
            # Converting to HTML block inside the <table> tag
            # It is middle part of body of the HTML template
            report = df.to_html()
            tab = string_snippets.tab_report + report
        elif type(self.db_data) is str:
            tab = f'\t<p class="center-top-text">{self.db_data}</p>\n'
        else:
            tab = string_snippets.system_error
        # Updating template by overwriting when get the new data from KIS
        with open(r'C:\Users\adm-ryadovoyaa\Documents\DMKprojects\MedVeiws\observer\WebApp\templates\output.html', 'wt',
                  encoding='utf-8') as template:
            template.write(ReadyReportHTML.top_of_template)
            template.writelines(tab)
            template.writelines(ReadyReportHTML.bot_of_template)
