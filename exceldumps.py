from xlsxwriter.workbook import Workbook
import os

# def dump_dict_list(filename, data, order=None):
#     if filename[0] == '/':
#         filename = filename.lstrip('/')
#     if not filename.endswith('.xlsx'):
#         filename += '.xlsx'
# Create an new Excel file and add a worksheet.
#     workbook = Workbook('exceldumps/'+filename, {'constant_memory': True})
#     worksheet = workbook.add_worksheet()
# Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 20)
# Add a bold format to highlight cell text.
# bold = workbook.add_format({'bold': 1})
# Write some simple text.
# worksheet.write('A1', 'Hello')
# Text with formatting.
# worksheet.write('A2', 'World', bold)
# Write some numbers, with row/column notation.
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)
#     if not order is None:
#         for i in xrange(len(order)):
#             worksheet.write(0, i, order[i])
#         for i in xrange(len(data)):
#             for j in xrange(len(order)):
#                 worksheet.write(i+1, j, data[i][order[j]])
#     else:
#         raise Exception, 'order should not be None, is unimplemented yet.'
#     workbook.close()
#     return os.path.abspath("exceldumps/"+filename)


def create_workbook(filename):
    if filename[0] == '/':
        filename = filename.lstrip('/')
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'
    # Create an new Excel file and add a worksheet.
    workbook = Workbook('exceldumps/' + filename, {'constant_memory': True})
    return workbook, os.path.abspath("exceldumps/" + filename)


def get_new_worksheet(workbook):
    return workbook.add_worksheet()


def write_to_worksheet(worksheet, data, order, startindex=0, skip_vals = {}):
    if not order is None:
        if startindex == 0:
            for i in xrange(len(order)):
                worksheet.write(0, i, order[i])
        moonwalk = 0
        for i in xrange(len(data)):
            gandalf = 0
            for key in skip_vals:
                for val in skip_vals[key]:
                    if val in data[i][key]:
                        gandalf = 1
            if gandalf:
                moonwalk += 1
                continue # thou shalt not pass
            for j in xrange(len(order)):
                current_col = order[j]
                current_val = data[i].get(current_col, 'None')
                worksheet.write(i - moonwalk + 1 + startindex,
                                j, current_val )
        return {"added": len(data) - moonwalk, "skipped": moonwalk}
    else:
        raise Exception('order should not be None, is unimplemented yet.')


def close_workbook(workbook):
    workbook.close()
