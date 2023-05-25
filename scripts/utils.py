import pygraphviz as pgv
from IPython.display import Image

def display_bayesian_model(model, file_path):
    graph = pgv.AGraph(directed=True)

    for node in model.nodes():
        graph.add_node(node)

    for edge in model.edges():
        graph.add_edge(*edge)

    graph.layout(prog='dot')
    graph.draw(file_path)

    return Image(filename=file_path)
