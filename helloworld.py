import streamlit as st
with st.echo(code_location='below'):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px

    name = st.text_input("Name", key="name", value="???")
    st.write(f"### Hello, {name}!")

    def get_data():
        data_url = "https://raw.githubusercontent.com/scientia-ipsa/pokemon_dataset/e078992fd3562d5a7ca51fdcf30976db4328c67c/pokemon.csv"
        return pd.read_csv(data_url)

    # Выбор типа - график между защитой/атакой.
    st.title('Choose your pokemon type!')

    st.write("Here you can choose the type of the pokemon and see the relation between the defense and attack of the pokemons of this type!")
    df = get_data()
    a = df.sort_values(by=['defense'])
    parameter = st.selectbox("Type", a['type1'].unique())
    fig, ax=plt.subplots()
    sns.lineplot(x='defense', y = 'attack', data=a.loc[a['type1'] == parameter], ax=ax)
    st.pyplot(fig)

    # Фильтрация покемонов по скорости.

    st.title('Choose the speed!')

    st.write("Here you can choose the speed of a pokémon. In the speed-attack axis will be all pokémon that have a speed no greater than the set one.")
    speed = st.slider('Speed',min_value=0, max_value=200)
    b=df.sort_values(by=['speed'])
    c = b.loc[b['speed'] <= speed]
    fig, ax=plt.subplots(1,1, figsize=(10,10))
    sns.scatterplot(data=c, x="speed", y="attack",hue = "type1", style="type1", ax=ax, edgecolor="black")
    st.pyplot(fig)
    c

    # Pokemon distribution.

    st.title('Interactive graph')

    st.write("In this diagram you can see the distribution of all chosen pokémon. Let's take a look how rare they are!")

    options = st.multiselect('Choose types',['bug','normal','water','grass', 'rock', 'ground', 'fairy', 'ghost', 'fire', 'psychic', 'dark', 'steel', 'poison', 'ice', 'fighting', 'electric', 'dragon', 'flying'], ['normal'])

    ax=plt.subplots()

    labels = options
    values = []
    sum = 0
    for element in labels:
        sum += len(df.loc[df['type1'] == element].index)
    for element in labels:
        values.append((len(df.loc[df['type1'] == element].index))/sum)

    fig = px.pie(values=values, names=labels)
    st.plotly_chart(fig)

    # Horizontal boxplot with observations

    st.title('Some boxplot data')

    st.write("Here you can find the graph of horizontal boxplot with pokemon observations")

    fig, ax=plt.subplots()
    x=[df['speed'], df['hp'], df['defense']]
    df = pd.DataFrame(x, index=['Speed', "HP", 'Defense'])

    df.T.boxplot(vert=False)
    plt.subplots_adjust(left=0.25)
    st.pyplot(fig)

    #One more interactive graph:

    st.title('Animation! One more interactive graph!')
    st.write("Here you can choose the pokemon generation and see their characteristics!")
    new = get_data()
    ax=plt.subplots()
    fig = px.scatter(new, x="attack", y="hp", animation_frame="generation", animation_group="name",
           size="defense", color="type1", hover_name="name", size_max=35, range_x=[0,200], range_y=[0,200],
           )
    st.plotly_chart(fig)

    st.write("Press the lucky button!")

    start_btn = st.button('Start')

    if start_btn:
        st.balloons()
        st.snow()
