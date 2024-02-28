import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

sg.theme('darkgray')

def create_layout(pt):
    checkboxes = [str(param.strip()) for param in pt]
    tab_layout_1 = [
        [
            sg.Column(
                [
                    [sg.Checkbox(text, key=f'CHECKBOX({i})', default="") for i, text in enumerate(checkboxes, start=1)]
                ],
                scrollable=True,
                size=(300, 80)
            )
        ]
    ]
    tab_1 = sg.Tab('Parameter', tab_layout_1)
    tab_group = sg.TabGroup([[tab_1]], enable_events=True, key='-TABGROUP-', tab_location='t')
    
    layout = [
        [
            sg.Column(
                [
                    [sg.Text('Real-Time Anomaly Detection', relief=sg.RELIEF_RIDGE, justification='center', font=("Constantia", 17, 'bold'))],
                    [sg.Frame("", layout=[[sg.Column([[tab_group], [sg.Button('Submit')]])]], vertical_alignment='top')],
                    [sg.Text("", key='-PARAMETER-', font=('Helvetica', 14))]
                ]
            ),
            sg.Column(
                [
                    [sg.Text('Anomalous Data', justification='center', font=("Constantia", 17, 'bold'))],
                    [sg.Multiline(size=(30, 10), key='-ANOMALIES-')]
                ],
                vertical_alignment='top'
            ),
            sg.Column(
                [
                    [sg.Text('Live Evaluation', justification='center', font=("Constantia", 17, 'bold'))],
                    [sg.Multiline(size=(30, 10), key='-EVALUATION-')]
                ],
                vertical_alignment='top'
            ),
            sg.Column(
                [
                    [sg.Text('Plots & Mitigation', justification='center', font=("Constantia", 17, 'bold'))],
                    [sg.Button('Generate Plots')]
                ],
                vertical_alignment='bottom',
                justification='center'
            )
        ]
    ]
    return layout

def update_plot(canvas, data_path='real_data.out'):
    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.loadtxt(data_path, usecols=(0, 1))
    ax.clear()
    ax.plot(x[:, 0], x[:, 1])
    ax.set_xlabel("Time (Sec)")
    ax.set_ylabel("")
    ax.set_title("")
    ax.grid()
    canvas.draw()

def main():
    f = open('dyn.out.txt', 'r')
    pt = f.readlines()
    f.close()

    scr_width, scr_height = sg.Window.get_screen_size()

    layout = create_layout(pt)

    window = sg.Window('Real-Time Anomaly Detection Software', layout, location=(0, 0), no_titlebar=False, size=(scr_width, scr_height), finalize=True)

    fig, ax = plt.subplots(figsize=(8, 4))
    canvas = FigureCanvasTkAgg(fig, window['f-CANVAS'].TKCanvas)
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Submit':
            window.close()
            checked_params = [key for key, value in values.items() if value and 'CHECKBOX' in key]
            layout = create_layout(pt)
            window = sg.Window('Real-Time Anomaly Detection Software', layout, location=(0, 0), no_titlebar=False, size=(scr_width, scr_height), finalize=True)
        elif event == 'Generate Plots':
            # Add code here to generate plots and implement mitigation actions
            sg.popup('Plots generated and mitigation actions implemented!')
        else:
            update_plot(canvas)
            # Update anomalies and evaluation (replace these with actual data)
            window['-ANOMALIES-'].update("Anomalous data goes here")
            window['-EVALUATION-'].update("Live evaluation parameters go here")

    window.close()

if __name__ == "__main__":
    main()
--------------------------------------------------------------------------------------------------------------------------------------------------

import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

sg.theme('darkgray')

def create_layout(pt):
    checkboxes = [str(param.strip()) for param in pt]
    tab_layout_1 = [
        [
            sg.Column(
                [
                    [sg.Checkbox(text, key=f'CHECKBOX({i})', default="") for i, text in enumerate(checkboxes, start=1)]
                ],
                scrollable=True,
                size=(300, 80)
            )
        ]
    ]
    tab_1 = sg.Tab('Parameter', tab_layout_1)
    tab_group = sg.TabGroup([[tab_1]], enable_events=True, key='-TABGROUP-', tab_location='t')
    
    layout = [
        [
            sg.Column(
                [
                    [sg.Text('Real-Time Anomaly Detection', relief=sg.RELIEF_RIDGE, justification='center', font=("Constantia", 17, 'bold'))],
                    [sg.Frame("", layout=[[sg.Column([[tab_group], [sg.Button('Submit')]])]], vertical_alignment='top')],
                    [sg.Text("", key='-PARAMETER-', font=('Helvetica', 14))]
                ]
            ),
            sg.Column(
                [
                    [sg.Text('Anomalous Data', justification='center', font=("Constantia", 17, 'bold'))],
                    [sg.Multiline(size=(30, 10), key='-ANOMALIES-')]
                ],
                vertical_alignment='top'
            ),
            sg.Column(
                [
                    [sg.Text('Live Evaluation', justification='center', font=("Constantia", 17, 'bold'))],
                    [sg.Multiline(size=(30, 10), key='-EVALUATION-')]
                ],
                vertical_alignment='top'
            )
        ]
    ]
    return layout

def update_plot(canvas, data_path='real_data.out'):
    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.loadtxt(data_path, usecols=(0, 1))
    ax.clear()
    ax.plot(x[:, 0], x[:, 1])
    ax.set_xlabel("Time (Sec)")
    ax.set_ylabel("")
    ax.set_title("")
    ax.grid()
    canvas.draw()

def main():
    f = open('dyn.out.txt', 'r')
    pt = f.readlines()
    f.close()

    scr_width, scr_height = sg.Window.get_screen_size()

    layout = create_layout(pt)

    window = sg.Window('Real-Time Anomaly Detection Software', layout, location=(0, 0), no_titlebar=False, size=(scr_width, scr_height), finalize=True)

    fig, ax = plt.subplots(figsize=(8, 4))
    canvas = FigureCanvasTkAgg(fig, window['f-CANVAS'].TKCanvas)
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Submit':
            window.close()
            checked_params = [key for key, value in values.items() if value and 'CHECKBOX' in key]
            layout = create_layout(pt)
            window = sg.Window('Real-Time Anomaly Detection Software', layout, location=(0, 0), no_titlebar=False, size=(scr_width, scr_height), finalize=True)
        else:
            update_plot(canvas)
            # Update anomalies and evaluation (replace these with actual data)
            window['-ANOMALIES-'].update("Anomalous data goes here")
            window['-EVALUATION-'].update("Live evaluation parameters go here")

    window.close()

if __name__ == "__main__":
    main()
------------------------------------------------------------------------------------------------------------

#main code: primary

import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

sg.theme('darkgray')

def main():
    f = open('dyn.out.txt', 'r')
    pt = f.readlines()
    f.close()
    
    scr_width, scr_height = sg.Window.get_screen_size()
    
    layout1 = [[sg.Text('Real-Time Anomaly Detection', relief=sg.RELIEF_RIDGE, justification='center', font=("Constantia", 17, 'bold'), size=(scr_width, 0))]]
    layout2 = [[sg.TabGroup([[sg.Tab(str('Result'), [[sg.Canvas(key='f-CANVAS', size=(800, 400))]])]])]]
    
    checkboxes = [str(pt[i].strip()) for i in range(len(pt))]
    tab_layout_1 = [
    [
        sg.Column(
            [
                [
                    sg.Checkbox(text, key=f'CHECKBOX({i})', default="")
                    for i, text in enumerate(checkboxes[:len(pt)], start=1)
                ]
            ],
            scrollable=True,
            size=(300, 80)
        )
    ]
]

    tab_1 = sg.Tab('Parameter', tab_layout_1)
    tab_group = sg.TabGroup([[tab_1]], enable_events=True, key='-TABGROUP-', tab_location='t')
    
    layout3 = [[tab_group], [sg.Button('Submit')]]
    
    layout_1 = [[sg.Column([[sg.Column(layout1)], [sg.Frame("", layout=[[sg.Column(layout2)]])]]),
                 sg.Column([[sg.Frame("", layout=[[sg.Column(layout3)]])]], vertical_alignment='top'),
                 sg.Column([[sg.Text("", key='-PARAMETER-', font=('Helvetica', 14))]], vertical_alignment='top')]]

    window = sg.Window('Real-Time Anomaly Detection Software', layout_1, location=(0, 0), no_titlebar=False, size=(scr_width, scr_height), finalize=True)

    fig, ax = plt.subplots(figsize=(8, 4))
    canvas = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    while True:
        event, values = window.read(True)
        if event == sg.WINDOW_CLOSED or event == 'Exit' or event is None:
            break
        elif event == 'Submit':
            window.close()
            checked_value = [key for key, value in values.items() if value]
            layout_1 = [[sg.Text('Real-Time Anomaly Detection', relief=sg.RELIEF_RIDGE, justification='center', font=("Constantia", 17, 'bold'), size=(scr_width, 0))]]
            layout2 = [[sg.TabGroup([[sg.Tab(str('Result'), [[sg.Canvas(key='f-CANVAS', size=(800, 400))]])]])]]
            checkboxes = [str(pt[i].strip()) for i in range(len(pt))]
            tab_layout_1 = [
    [
        sg.Column(
            [
                [sg.Checkbox(text, key=f'CHECKBOX({i})', default="") for i, text in enumerate(checkboxes[:len(pt)], start=1)]
            ],
            scrollable=True,
            size=(300, 80)
        )
    ]
]

            tab_1 = sg.Tab('Parameter', tab_layout_1)
            tab_group = sg.TabGroup([[tab_1]], enable_events=True, key='-TABGROUP-', tab_location='t')
            layout3 = [[tab_group], [sg.Button('Submit')]]
            layout_1 = [[sg.Column([[sg.Column(layout1)], [sg.Frame("", layout=[[sg.Column(layout2)]])]]),
                         sg.Column([[sg.Frame("", layout=[[sg.Column(layout3)]])]], vertical_alignment='top'),
                         sg.Column([[sg.Text("", key='-PARAMETER-', font=('Helvetica', 14))]], vertical_alignment='top')]]
            window = sg.Window('Real-Time Anomaly Detection Software', layout_1, location=(0, 0), no_titlebar=False, size=(scr_width, scr_height), finalize=True)
        else:
            fig, ax = plt.subplots(figsize=(8, 4))
            canvas = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
            canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
            x = np.loadtxt('real_data.out', usecols=(0, 1))
            ax.clear()
            ax.plot(x[:, 0], x[:, 1])
            ax.set_xlabel("Time (Sec)")
            ax.set_ylabel("")
            ax.set_title("")
            ax.grid()
            canvas.draw()
            window.close()

if __name__ == "__main__":
    main()

