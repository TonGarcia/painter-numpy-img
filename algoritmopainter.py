# -*- coding: utf-8 -*-
"""AlgoritmoPainter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N4tnRIUoKBBerfRIY2IONOg5iMxpA6kt

# Pintando Pixels Vizinhos

Para alterar este arquivo você precisa fazer uma cópia dele no seu Google Drive.

**IMPORTANTE**: Apenas altere a cécula da sua função paint, não altere as demais.

## Funcionamento dos eixos X e Y em imagens

![image.png](data:image/png;base64,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)
"""

from copy import copy, deepcopy
import matplotlib.pyplot as plt

# import IPython
#
# def configure_plotly_browser_state():
#   import IPython
#   display(IPython.core.display.HTML('''
#         <script src="/static/components/requirejs/require.js"></script>
#         <script>
#           requirejs.config({
#             paths: {
#               base: '/static/base',
#               plotly: 'https://cdn.plot.ly/plotly-latest.min.js?noext',
#             },
#           });
#         </script>
#         '''))
#
# IPython.get_ipython().events.register('pre_run_cell', configure_plotly_browser_state)

"""## Criação da Imagem"""

from PIL import Image
import numpy as np

# boolean matrix
matrix = np.random.randint(2, size=(25,25))
matrix_b = matrix.astype(bool)
matrix_i = matrix.astype(int)
img =  Image.fromarray(matrix_b)
iimg =  Image.fromarray(matrix_i, mode='L')
imgplot = plt.imshow(img)
plt.show()
# imgplot = plt.imshow(iimg)
# plt.show()

"""# Listagem das linhas da Imagem (1ª linha (eixo Y) na coluna 0 (x=0))"""

x=0
matrix_b[x]

"""## Crie sua função de paint"""

def paint(x, y, matrix):
    """
      Template
    """
    new_matrix = matrix[:]
    # TODO
    return new_matrix

def paint(x, y, matrix):
    """
      Solução Possível
    """
    new_matrix = deepcopy(matrix)

    counter = 0
    position_val = new_matrix[x][y]
    next_x, prev_x, next_y, prev_y = None, None, None, None

    stop_x_greater = False
    stop_x_less = False
    stop_y_greater = False
    stop_y_less = False

    while True:
        counter = counter + 1
        # Navega na linha
        if not stop_x_greater:
            next_x = x + counter
        if not stop_x_less:
            prev_x = x - counter
        # Navega na coluna
        if not stop_y_greater:
            next_y = y + counter
        if not stop_y_less:
            prev_y = y - counter

        # Check max & min positions
        minimal_x = prev_x <= 0
        maximal_x = next_x >= len(new_matrix)
        minimal_y = prev_y <= 0
        maximal_y = next_y >= len(new_matrix[0])

        if minimal_x:
            stop_x_less = True
        if maximal_x:
            stop_x_greater = True
        if minimal_y:
            stop_y_less = True
        if maximal_y:
            stop_y_greater = True

        if minimal_x and maximal_x and minimal_y and maximal_y:
            break

        prev_x_point_v = new_matrix[prev_x][y]
        next_x_point_v = new_matrix[next_x][y]

        prev_y_point_v = new_matrix[x][prev_y]
        next_y_point_v = new_matrix[x][next_y]

        prev_xy_point_v = new_matrix[prev_x][prev_y]
        next_xy_point_v = new_matrix[next_x][next_y]

        if prev_x_point_v != position_val and not stop_x_less:
            new_matrix[prev_x][y] = position_val
        else:
            stop_x_less = True
        if prev_y_point_v != position_val and not stop_y_less:
            new_matrix[x][prev_y] = position_val
        else:
            stop_y_less = True
        if next_x_point_v != position_val and not stop_x_greater:
            new_matrix[next_x][y] = position_val
        else:
            stop_x_greater = True
        if next_y_point_v != position_val and not stop_y_greater:
            new_matrix[x][next_y] = position_val
        else:
            stop_y_greater = True

    return new_matrix


def paint(x, y, matrix):
    """
      Solução Possível
    """
    new_matrix = deepcopy(matrix)

    counter = 0
    position_val = new_matrix[x][y]
    next_x, prev_x, next_y, prev_y = None, None, None, None
    max_len_x, max_len_y = len(new_matrix), len(new_matrix[0])
    stop_x_greater, stop_x_less, stop_y_greater, stop_y_less = False, False, False, False

    while True:
        counter = counter + 1
        next_x, prev_x, next_y, prev_y = x+counter, x-counter, y+counter, y-counter
        minimal_x, maximal_x, minimal_y, maximal_y = prev_x <= 0, next_x >= max_len_x, prev_y <= 0, next_y >= max_len_y

        if minimal_x and maximal_x and minimal_y and maximal_y:
            break

        if not maximal_x:
            last_max_x = next_x
            nxy = new_matrix[next_x][y]
            if nxy == position_val or stop_x_greater:
                stop_x_greater = True
            else:
                new_matrix[next_x][y] = position_val

        if not minimal_x:
            last_min_x = prev_x
            pxy = new_matrix[prev_x][y]
            if pxy == position_val or stop_x_less:
                stop_x_less = True
            else:
                new_matrix[prev_x][y] = position_val
        if not maximal_y:
            last_max_y = next_y
            nyx = new_matrix[x][next_y]
            if nyx == position_val or stop_y_greater:
                stop_y_greater = True
            else:
                new_matrix[x][next_y] = position_val
        if not minimal_y:
            last_min_y = prev_y
            pyx = new_matrix[x][prev_y]
            if pyx == position_val or stop_y_less:
                stop_y_less = True
            else:
                new_matrix[x][prev_y] = position_val

        if not stop_x_less and not stop_y_less:
            if new_matrix[prev_x][prev_y] != position_val:
                new_matrix[prev_x][prev_y] = position_val
        if not stop_x_greater and not stop_y_greater:
            if new_matrix[next_x][next_y] != position_val:
                new_matrix[next_x][next_y] = position_val


    return new_matrix


"""## Teste sua função"""

new_matrix = paint(x=0, y=0, matrix=matrix_b)
fig, axs = plt.subplots(1, 2, figsize=(10, 3))
n_img =  Image.fromarray(new_matrix)
axs[0].imshow(img)
axs[0].set_title('Imagem ORIGINAL')
axs[0].grid(False) # False = elimina as guias, True = adiciona linhas guias para facilitar de ver aonde foi pintado
axs[1].imshow(n_img)
axs[1].set_title('SUA Imagem')
axs[1].grid(False) # False = elimina as guias, True = adiciona linhas guias para facilitar de ver aonde foi pintado
plt.show()