# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:26:14 2022

@author: Madhavan
"""
from mendeleev.vis import create_vis_dataframe, periodic_table_bokeh
import seaborn as sns
from matplotlib import colors
import streamlit as st
from bokeh.plotting import show, output_notebook
from bokeh import palettes
from mendeleev.fetch import fetch_table
from mendeleev import element
from bokeh.events import ButtonClick

st.markdown("# Periodic table")
colormap_list=['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'crest', 'crest_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'flare', 'flare_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r']
colormap = st.sidebar.selectbox('colormap',colormap_list,index=10,help='Select a color map. Some are aesthetically pleasing others show better contrast and are suitable for visualisation')
elements = create_vis_dataframe()
ptable = fetch_table('elements')
cols = ['atomic_number', 'atomic_radius', 'atomic_volume',
        'boiling_point', 'density', 'dipole_polarizability',
       'electron_affinity', 'electronic_configuration', 'evaporation_heat',
       'fusion_heat', 'lattice_constant', 'lattice_structure',
       'melting_point', 'period', 'series_id',
       'specific_heat_capacity', 'thermal_conductivity',
       'vdw_radius', 'covalent_radius_cordero', 'covalent_radius_pyykko',
       'en_pauling', 'en_allen', 'jmol_color', 'cpk_color', 'proton_affinity',
       'gas_basicity', 'heat_of_formation', 'c6', 'covalent_radius_bragg',
       'vdw_radius_bondi', 'vdw_radius_truhlar', 'vdw_radius_rt',
       'vdw_radius_batsanov', 'vdw_radius_dreiding', 'vdw_radius_uff',
       'vdw_radius_mm3', 'abundance_crust', 'abundance_sea', 'molcas_gv_color',
       'en_ghosh', 'vdw_radius_alvarez', 'c6_gb', 'atomic_weight',
       'atomic_weight_uncertainty', 'is_monoisotopic', 'is_radioactive', 'cas',
       'atomic_radius_rahm', 'geochemical_class', 'goldschmidt_class',
       'metallic_radius', 'metallic_radius_c12',
       'covalent_radius_pyykko_double', 'covalent_radius_pyykko_triple',
       'discoverers', 'discovery_year', 'discovery_location', 'name_origin',
       'sources', 'uses', 'mendeleev_number', 'dipole_polarizability_unc',
       'pettifor_number', 'glawe_number', 'molar_heat_capacity']

prop = st.sidebar.selectbox('Element property',cols,index=0,help='Select a property to color the peridic table in similar groups.')
fig = periodic_table_bokeh(elements,attribute=prop, colorby='attribute',
              title=str(prop), cmap=colormap)
st.bokeh_chart(fig,use_container_width=False)
selection = st.sidebar.selectbox('Elements',elements.name[:],index=0,help='pick an element to show all details in database.')
cite = "_**mendeleev2014, author = {Mentel, Łukasz},title = {{mendeleev} -- A Python resource for properties of chemical elements, ions and isotopes},    url = {https://github.com/lmmentel/mendeleev},version = {0.11.0},date = {2014--}**_"
ls = [ 'atomic_number', 'atomic_radius', 'atomic_volume',
       'block', 'boiling_point', 'density', 'description',
       'dipole_polarizability', 'electron_affinity','evaporation_heat', 'fusion_heat','group_id', 'lattice_constant', 'lattice_structure', 'melting_point',
       'name', 'period', 'specific_heat_capacity', 'symbol',
       'thermal_conductivity', 'vdw_radius', 'covalent_radius_cordero',
       'covalent_radius_pyykko', 'en_pauling', 'en_allen', 'jmol_color',
       'cpk_color', 'proton_affinity', 'gas_basicity', 'heat_of_formation',
       'c6', 'covalent_radius_bragg', 'vdw_radius_bondi', 'vdw_radius_truhlar',
       'vdw_radius_rt', 'vdw_radius_batsanov', 'vdw_radius_dreiding',
       'vdw_radius_uff', 'vdw_radius_mm3', 'abundance_crust', 'abundance_sea',
       'molcas_gv_color', 'en_ghosh', 'vdw_radius_alvarez', 'c6_gb',
       'atomic_weight', 'atomic_weight_uncertainty', 'is_monoisotopic',
       'is_radioactive', 'cas', 'atomic_radius_rahm', 'geochemical_class',
       'goldschmidt_class', 'metallic_radius', 'metallic_radius_c12',
       'covalent_radius_pyykko_double', 'covalent_radius_pyykko_triple',
       'discoverers', 'discovery_year', 'discovery_location', 'name_origin',
       'sources', 'uses', 'mendeleev_number', 'dipole_polarizability_unc',
       'pettifor_number', 'glawe_number', 'molar_heat_capacity']
ele = element(selection)
st.markdown('### '+selection+' Properties')
for i in ls:
    expr = 'ele.'+i
    st.code('{}: {}'.format(i,eval(expr)))

#st.markdown('### _**all units are SI units**_')
st.markdown(cite)