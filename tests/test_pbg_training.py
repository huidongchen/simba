import simba as si
import pytest


@pytest.fixture
def adata_CG():
    return si.read_h5ad(
        "tests/data/preprocessed/rna_preprocessed.h5ad")


@pytest.fixture
def adata_CP():
    return si.read_h5ad(
        "tests/data/preprocessed/atac_preprocessed.h5ad")


def test_gen_graph(adata_CG, adata_CP, tmp_path):
    si.settings.set_workdir(tmp_path / "simba_rna")
    si.tl.gen_graph(list_CG=[adata_CG],
                    copy=False,
                    dirname='graph0')
    si.tl.gen_graph(list_CG=[adata_CG],
                    copy=False,
                    add_edge_weights=True,
                    dirname='graph1')
    si.tl.gen_graph(list_adata=[adata_CG],
                    copy=False,
                    dirname='graph2')
    si.tl.gen_graph(list_adata=[adata_CG],
                    copy=False,
                    add_edge_weights=True,
                    dirname='graph3')
    si.tl.gen_graph(list_adata=[adata_CG, adata_CP],
                    copy=False,
                    add_edge_weights=True,
                    dirname='graph4')


def test_pbg_training_rna(adata_CG, tmp_path):
    si.settings.set_workdir(tmp_path / "simba_rna")
    si.tl.gen_graph(list_CG=[adata_CG],
                    copy=False,
                    dirname='graph0')
    dict_config = si.settings.pbg_params.copy()
    si.settings.set_pbg_params(dict_config)
    si.tl.pbg_train(auto_wd=True,
                    output='model0')
    si.tl.pbg_train(auto_wd=True,
                    use_edge_weights=True,
                    output='model1')
    si.load_graph_stats()
    si.load_pbg_config()
    si.pl.pbg_metrics(fig_ncol=1,
                      save_fig=True)


def test_pbg_training_atac(adata_CP, tmp_path):
    si.settings.set_workdir(tmp_path / "simba_atac")
    si.tl.gen_graph(list_CP=[adata_CP],
                    copy=False,
                    dirname='graph0')
    si.tl.pbg_train(auto_wd=True,
                    output='model')
    si.pl.pbg_metrics(fig_ncol=1,
                      save_fig=True)
