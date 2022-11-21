import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from chart_studio.plotly import plot, iplot
from dash import Dash  # pip install dash (version 2.0.0 or higher)
from dash import dcc, html

app = Dash(__name__)

df = pd.read_csv('Main.csv')
df = df.sort_values(by=['Club_Name'])

main_df= df
df1 = df.drop(['Event_x','Role_x','Fest_Name_x', 'Event_y', 'Fest_Name_y', 'Role_y'], axis=1)
df1 = df1.drop_duplicates()
df1 = df1.fillna('NA')
df1 = df1.sort_values(by=['Club_Name'])

df2 = df.drop(['Fest_Name_x', 'Event_y', 'Fest_Name_y', 'Role_y'], axis=1)
df2 = df2.drop_duplicates()
df2 = df2.sort_values(by=['Event_x'])

df3 = df.drop(['Club_Name','Event_x','Role_x','Fest_Name_y', 'Role_y'], axis=1)
df3 = df3.drop_duplicates()
df3 = df3.sort_values(by=['Fest_Name_x'])

df4 = df.drop(['Club_Name','Event_x','Event_y','Role_x','Fest_Name_y', 'Role_y'], axis=1)
df4 = df4.drop_duplicates()
df4 = df4.fillna('NA')
df4 = df4.sort_values(by=['Fest_Name_x'])

M_Fests = df3['Event_y'].value_counts().sort_index()
N_fests = df3['Fest_Name_x'].value_counts().sort_index()
M_Clubs = df2['Event_x'].value_counts().sort_index()


dfc ={}
for club in df2['Club_Name'].unique():
    dfc[club]=df2[df2['Club_Name'] == club]

eve={}

for club in df2['Club_Name'].unique():
    dfc[club]=df2[df2['Club_Name'] == club]
    eve[club]={}
    for event in dfc[club]['Event_x'].unique():
        eve[club][event]=dfc[club][dfc[club]['Event_x'] == event]

R={}
N_R={}
p={}
lis=[]

for club in df2['Club_Name'].unique():
    R[club]={}
    N_R[club]={}
    p[club]={}
    for event in dfc[club]['Event_x'].unique():
        R[club][event]=eve[club][event].Role_x.value_counts().sort_index()
        N_R[club][event]=list(R[club][event])
        lis.append(N_R[club][event])


Roles=df2.Role_x.value_counts().sort_index()
# print(Roles.index)

N_M_clubs = df1['Club_Name'].value_counts().sort_index()
# print(N_M_clubs)
M_clubs= list(N_M_clubs)
# print(M_clubs)
# print(N_M_clubs.index)

N_roles = df2['Role_x'].value_counts().sort_index()
# print(N_roles)

df_club = pd.DataFrame({
    "Clubs": N_M_clubs.index,
    "Members": M_clubs
})

N_events_club=df2['Event_x'].value_counts().sort_index()
M_events=list(N_events_club)

# print(M_events)
# print(N_events_club.index)
#print(N_events_club.index[6:9])


df_event = pd.DataFrame({
    "Event_Club_1": N_events_club.index[:3],
    "M_Club1_event": M_events[:3],
    "Event_Club_2": N_events_club.index[3:6],
    "M_Club2_event": M_events[3:6],
    "Event_Club_3": N_events_club.index[6:9],
    "M_Club3_event": M_events[6:9]
})

df_role = pd.DataFrame(lis, columns =Roles.index) 
df_role['Events'] = N_events_club.index
df_role = df_role.fillna(0)
df_role['Total_Organisers'] = df_role['organiser_1'] + df_role['organiser_2'] + df_role['organiser_3'] + df_role['organiser_4'] + df_role['organiser_5']
N_events = df_role['Events']
N_partisipants = df_role['Participant']
N_organisers = df_role['Total_Organisers']
# print(df_role)

N_M_fests = df4['Fest_Name_x'].value_counts().sort_index()
# print(N_M_fests)
P_fests= list(N_M_fests)


df_fest = pd.DataFrame({
    "Fest": N_M_fests.index,
    "Members": P_fests
})
df_fest = df_fest.drop_duplicates()
# print(df_fest)

N_events_fest=df3['Event_y'].value_counts().sort_index()
M_events_fest=list(N_events_fest)
# print(N_events_fest)

df_fest_event_1 = pd.DataFrame({
    "Event_fest_1": N_events_fest.index[:13],
    "M_fest1_event": M_events_fest[:13]

})

df_fest_event_2 = pd.DataFrame({
    "Event_fest_2": N_events_fest.index[13:28],
    "M_fest2_event": M_events_fest[13:28]
})

N_F = M_Fests.index
N_C = M_Clubs.index

N_C_list = list(N_C)

N_F_list = list(N_F)

list1 = []
for i in range(28):
    if i < 13:
        a = "fest_1"
        list1.append(a)
    else:
        b = "fest_2"
        list1.append(b)
list2 = []
for i in range(9):
    if i < 3:
        a = "club_1"
        list2.append(a)
    elif i < 6:
        b = "club_2"
        list2.append(b)
    else:
        c = "club_3"
        list2.append(c)


total = dict(zip(list1, N_F_list))
M_fests = list(M_Fests)


df_fests = pd.DataFrame({
    "Fest_Event": M_Fests.index,
    "Members": M_Fests,
    "Fests": list1
})
df_clubs = pd.DataFrame({
    "Club_Event": M_Clubs.index,
    "Members": M_Clubs,
    "Clubs": list2


})



fig = px.bar(df_club, x="Clubs", y="Members", barmode="group")
fig.update_layout(bargap = 0.6)
fig1 = px.pie(df_event, values="M_Club1_event", names="Event_Club_1",hole = 0.4)
fig2 = px.pie(df_event, values="M_Club2_event", names="Event_Club_2",hole = 0.4)
fig3 = px.pie(df_event, values="M_Club3_event", names="Event_Club_3",hole = 0.4)
fig4 = px.bar(df_fest, x="Fest", y="Members", barmode="group")
fig5 = px.bar(df_fest_event_1, x="Event_fest_1", y="M_fest1_event", barmode="group")
fig4.update_layout(bargap = 0.6)
fig6 = px.bar(df_fest_event_2, x="Event_fest_2", y="M_fest2_event", barmode="group")
fig7 = px.scatter(df_fests, x="Fest_Event", y="Members",color="Fests", size='Members',hover_data=['Fest_Event', 'Members'])
fig8 = px.scatter(df_clubs, x="Club_Event", y="Members",color="Clubs", size='Members',hover_data=['Club_Event', 'Members'])



fig1.add_annotation(x= 0.5, y = 0.5,
                    text = '<b>Club_1</b>',
                    font = dict(size=12,family='Verdana', 
                                color='black'),
                    showarrow = False)
fig2.add_annotation(x= 0.5, y = 0.5,
                    text = '<b>Club_2</b>',
                    font = dict(size=12,family='Verdana', 
                                color='black'),
                    showarrow = False)
fig3.add_annotation(x= 0.5, y = 0.5,
                    text = '<b>Club_3</b>',
                    font = dict(size=12,family='Verdana', 
                                color='black'),
                    showarrow = False)

trace1 = go.Bar(x= N_events,y= N_partisipants,name='Participants')
trace2 = go.Bar(x=N_events,y=N_organisers,name='Organizers')

app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Clubs'),

        html.Div(children='''
            Members in each club.
        '''),

        dcc.Graph(id='graph1',figure=fig,style={'display': 'inline-block',"height":400,"width":750,}),
        dcc.Graph(id='graph1',figure=fig8,style={'display': 'inline-block',"height":400,"width":750,})
    ]),

     html.Div([
        html.H1(className='row',children='Club_Events'),

        html.Div(children='''
            Club Members in each event.
        '''),

        dcc.Graph(id='graph2',figure=fig1,style={'display': 'inline-block',"height":275,"width":500,}),
        dcc.Graph(id='graph2',figure=fig2,style={'display': 'inline-block',"height":275,"width":500}),
        dcc.Graph(id='graph2',figure=fig3,style={'display': 'inline-block',"height":275,"width":500})
    ]),

    html.Div([
        html.H1(className='row',children='Roles'),

        html.Div(children='''
            Roles in each event.
        '''),
        dcc.Graph(id='bar_plot',figure=go.Figure(data=[trace1, trace2],layout=go.Layout(barmode='stack'))),
    ]),

    html.Div([
        html.H1(children='Fests'),
        html.Div(children='''
            Members in each fest.
        '''),

        dcc.Graph(id='graph1',figure=fig4,style={'display': 'inline-block',"height":400,"width":750,}),
        dcc.Graph(id='graph1',figure=fig7,style={'display': 'inline-block',"height":400,"width":750,})
    ]),
   
     html.Div([
        html.H1(className='row',children='Fest_Events'),

        html.Div(children='''
            Fest Members in each event.
        '''),

        dcc.Graph(id='graph2',figure=fig5,style={'display': 'inline-block',"height":400,"width":750,}),
        dcc.Graph(id='graph2',figure=fig6,style={'display': 'inline-block',"height":400,"width":750,})
    ])

])


if __name__ == '__main__':
    app.run_server(debug=True)