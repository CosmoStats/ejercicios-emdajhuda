from getdist import loadMCSamples, plots

base = '/Users/juda/lab_alma/proyecto_final/chains'

# ----------------------------------------------------------------------
# 1) Triangle plots individuales, con título indicando modelo + dataset
# ----------------------------------------------------------------------

runs = [
    # (path relativo a base, parametros a graficar, titulo, nombre de archivo)
    ('proyecto_only_desibao/proyecto_only_desibao',
     ['H0', 'omega_b', 'omega_cdm'],
     'FlatLCDM — DESI BAO',
     'triangle_plot_only_desibao.png'),

    ('proyecto_only_desibao/proyecto_only_desibao_ok',
     ['H0', 'omega_b', 'omega_cdm', 'Omega_k_1000'],
     'LCDM + $\\Omega_k$ — DESI BAO',
     'triangle_plot_only_desibao_ok.png'),

    ('proyecto_only_desibao/proyecto_only_desibao_w',
     ['H0', 'omega_b', 'omega_cdm', 'w'],
     'wCDM — DESI BAO',
     'triangle_plot_only_desibao_w.png'),

    ('proyecto_only_desibao/proyecto_only_desibao_w0wa',
     ['H0', 'omega_b', 'omega_cdm', 'w', 'wa'],
     'w0waCDM — DESI BAO',
     'triangle_plot_only_desibao_w0wa.png'),

    ('proyecto_only_desibao/proyecto_only_desibao_w0wa_ok',
     ['H0', 'omega_b', 'omega_cdm', 'w', 'wa', 'Omega_k_1000'],
     'w0waCDM + $\\Omega_k$ — DESI BAO',
     'triangle_plot_only_desibao_w0wa_ok.png'),

    ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s',
     ['H0', 'omega_b', 'omega_cdm'],
     'FlatLCDM — DESI BAO + Pantheon+',
     'triangle_plot_only_desibao_p+s.png'),

    ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_ok',
     ['H0', 'omega_b', 'omega_cdm', 'Omega_k_1000'],
     'LCDM + $\\Omega_k$ — DESI BAO + Pantheon+',
     'triangle_plot_only_desibao_p+s_ok.png'),

    ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w',
     ['H0', 'omega_b', 'omega_cdm', 'w'],
     'wCDM — DESI BAO + Pantheon+',
     'triangle_plot_only_desibao_p+s_w.png'),

    ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w0wa',
     ['H0', 'omega_b', 'omega_cdm', 'w', 'wa'],
     'w0waCDM — DESI BAO + Pantheon+',
     'triangle_plot_only_desibao_p+s_w0wa.png'),

    ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w0wa_ok',
     ['H0', 'omega_b', 'omega_cdm', 'w', 'wa', 'Omega_k_1000'],
     'w0waCDM + $\\Omega_k$ — DESI BAO + Pantheon+',
     'triangle_plot_only_desibao_p+s_w0wa_ok.png'),

    ('proyecto_only_desibao_cmb/proyecto_only_desibao_cmb',
     ['H0', 'omega_b', 'omega_cdm'],
     'FlatLCDM — DESI BAO + Planck CMB',
     'triangle_plot_only_desibao_cmb.png'),

    ('proyecto_only_desibao_cmb/proyecto_only_desibao_cmb_ok',
     ['H0', 'omega_b', 'omega_cdm', 'Omega_k_1000'],
     'LCDM + $\\Omega_k$ — DESI BAO + Planck CMB',
     'triangle_plot_only_desibao_cmb_ok.png'),
]

for rel_path, params, title, outfile in runs:
    samples = loadMCSamples(f'{base}/{rel_path}')
    g = plots.get_subplot_plotter()
    g.triangle_plot(samples, params, filled=True)
    g.fig.suptitle(title, fontsize=16)
    g.fig.tight_layout(rect=[0, 0, 1, 0.95])
    g.fig.savefig(outfile, bbox_inches='tight')


# ----------------------------------------------------------------------
# 2) Graficas comparativas: mismo modelo, distintos conjuntos de datos
#    superpuestos en un solo triangle plot con colores distintos
# ----------------------------------------------------------------------

comparisons = [
    # (lista de (path, etiqueta legend), parametros, titulo, nombre de archivo)
    (
        [
            ('proyecto_only_desibao/proyecto_only_desibao', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s', 'DESI BAO + Pantheon+'),
        ],
        ['Omega_m', 'H0'],
        'FlatLCDM — Comparación de conjuntos de datos',
        'compare_flatlcdm_omegam_H0.png',
    ),
    (
        [
            ('proyecto_only_desibao/proyecto_only_desibao_ok', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_ok', 'DESI BAO + Pantheon+'),
        ],
        ['Omega_m', 'H0'],
        'LCDM + $\\Omega_k$ — Comparación de conjuntos de datos',
        'compare_lcdm_ok_omegam_H0.png',
    ),
    (
        [
            ('proyecto_only_desibao/proyecto_only_desibao_w', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w', 'DESI BAO + Pantheon+'),
        ],
        ['Omega_m', 'H0'],
        'wCDM — Comparación de conjuntos de datos',
        'compare_wcdm_omegam_H0.png',
    ),
    (
        [
            ('proyecto_only_desibao/proyecto_only_desibao_w0wa', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w0wa', 'DESI BAO + Pantheon+'),
        ],
        ['Omega_m', 'H0'],
        'w0waCDM — Comparación de conjuntos de datos',
        'compare_w0wacdm_omegam_H0.png',
    ),
    (
        [
            ('proyecto_only_desibao/proyecto_only_desibao_w0wa_ok', 'DESI BAO'),
            ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w0wa_ok', 'DESI BAO + Pantheon+'),
        ],
        ['Omega_m', 'H0'],
        'w0waCDM + $\\Omega_k$ — Comparación de conjuntos de datos',
        'compare_w0wacdm_ok_omegam_H0.png',
    ),
]

for run_list, params, title, outfile in comparisons:
    samples_list = [loadMCSamples(f'{base}/{rel_path}') for rel_path, _ in run_list]
    legend_labels = [label for _, label in run_list]

    g = plots.get_subplot_plotter()
    g.triangle_plot(
        samples_list,
        params,
        filled=True,
        legend_labels=legend_labels,
        contour_colors=['tab:blue', 'tab:orange'],
    )
    g.fig.suptitle(title, fontsize=16)
    g.fig.tight_layout(rect=[0, 0, 1, 0.95])
    g.fig.savefig(outfile, bbox_inches='tight')


# ----------------------------------------------------------------------
# 3) Comparacion extra: w0 y wa del modelo w0waCDM, DESI BAO vs DESI+P+S
# ----------------------------------------------------------------------

w0wa_runs = [
    ('proyecto_only_desibao/proyecto_only_desibao_w0wa', 'DESI BAO'),
    ('proyecto_only_desibao_p+s/proyecto_only_desibao_p+s_w0wa', 'DESI BAO + Pantheon+'),
]

samples_list = [loadMCSamples(f'{base}/{rel_path}') for rel_path, _ in w0wa_runs]
legend_labels = [label for _, label in w0wa_runs]

g = plots.get_subplot_plotter()
g.triangle_plot(
    samples_list,
    ['w', 'wa'],
    filled=True,
    legend_labels=legend_labels,
    contour_colors=['tab:blue', 'tab:orange'],
)
g.fig.suptitle('w0waCDM — Comparación $w_0$, $w_a$ entre conjuntos de datos', fontsize=16)
g.fig.tight_layout(rect=[0, 0, 1, 0.90])
g.fig.savefig('compare_w0wacdm_w0_wa.png', bbox_inches='tight')