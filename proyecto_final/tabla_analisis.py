from getdist import loadMCSamples

base = '/Users/juda/lab_alma/proyecto_final/chains'
outfile = 'tabla_resumen.tex'

# ----------------------------------------------------------------------
# Definición de cada fila: (ruta, nombre del modelo, nombre del dataset,
# lista de parametros que aplican para ese modelo, de los 5 posibles)
# ----------------------------------------------------------------------

ALL_PARAMS = ['H0', 'Omega_m', 'Omega_k_1000', 'w', 'wa']

# ----------------------------------------------------------------------
# Definicion agrupada por modelo: cada bloque tiene un nombre de modelo,
# los parametros que le aplican, y la lista de (ruta, nombre_dataset)
# ----------------------------------------------------------------------

blocks = [
    {
        'model_name': 'FlatLCDM',
        'params': ['H0', 'Omega_m'],
        'datasets': [
            ('proyecto_only_desibao/proyecto_only_desibao', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s', 'DESI BAO + P+'),
            ('proyecto_only_desibao_cmb/proyecto_only_desibao_cmb', 'DESI BAO + CMB'),
        ],
    },
    {
        'model_name': 'LCDM + $\\Omega_k$',
        'params': ['H0', 'Omega_m', 'Omega_k_1000'],
        'datasets': [
            ('proyecto_only_desibao/proyecto_only_desibao_ok', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_ok', 'DESI BAO + P+'),
            ('proyecto_only_desibao_cmb/proyecto_only_desibao_cmb_ok', 'DESI BAO + CMB'),
        ],
    },
    {
        'model_name': 'wCDM',
        'params': ['H0', 'Omega_m', 'w'],
        'datasets': [
            ('proyecto_only_desibao/proyecto_only_desibao_w', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w', 'DESI BAO + P+'),
        ],
    },
    {
        'model_name': 'w0waCDM',
        'params': ['H0', 'Omega_m', 'w', 'wa'],
        'datasets': [
            ('proyecto_only_desibao/proyecto_only_desibao_w0wa', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w0wa', 'DESI BAO + P+'),
        ],
    },
    {
        'model_name': 'w0waCDM + $\\Omega_k$',
        'params': ['H0', 'Omega_m', 'Omega_k_1000', 'w', 'wa'],
        'datasets': [
            ('proyecto_only_desibao/proyecto_only_desibao_w0wa_ok', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w0wa_ok', 'DESI BAO + P+'),
        ],
    },
]


def get_value_string(samples, param):
    """
    Devuelve 'media^{+sup}_{-inf}' con el percentil 68% (1 sigma),
    usando las marginalizadas de getdist. Si el parametro no existe
    en las cadenas, devuelve '-'.
    """
    try:
        margestats = samples.getMargeStats()
        par = margestats.parWithName(param)
        if par is None:
            return '-'
        mean = par.mean
        # limits[0] contiene el intervalo al 68% (1 sigma) por defecto en getdist
        lim = par.limits[0]
        lower = lim.lower
        upper = lim.upper
        plus = upper - mean
        minus = mean - lower
        return f'${mean:.4f}^{{+{plus:.4f}}}_{{-{minus:.4f}}}$'
    except Exception:
        return '-'


# ----------------------------------------------------------------------
# Construcción de la tabla
# ----------------------------------------------------------------------

lines = []
lines.append(r'\begin{table}[H]')
lines.append(r'    \centering')
lines.append(r'    \caption{Valores centrales (media) e incertidumbres (68\% C.L.) por modelo y dataset.}')
lines.append(r'    \label{tab:resumen}')
lines.append(r'    \begin{tabular}{lccccc}')
lines.append(r'        \toprule')
lines.append(r'        Dataset & $H_0$ & $\Omega_m$ & $10^3\Omega_k$ & $w$ & $w_a$ \\')

for i, block in enumerate(blocks):
    lines.append(r'        \midrule')
    lines.append(r'        \multicolumn{6}{l}{\textbf{' + block['model_name'] + r'}} \\')
    lines.append(r'        \midrule')

    for rel_path, dataset_name in block['datasets']:
        samples = loadMCSamples(f'{base}/{rel_path}')

        values = []
        for param in ALL_PARAMS:
            if param in block['params']:
                values.append(get_value_string(samples, param))
            else:
                values.append('-')

        row_str = f'        {dataset_name} & ' + ' & '.join(values) + r' \\'
        lines.append(row_str)

lines.append(r'        \bottomrule')
lines.append(r'    \end{tabular}')
lines.append(r'\end{table}')

with open(outfile, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Tabla guardada en {outfile}')