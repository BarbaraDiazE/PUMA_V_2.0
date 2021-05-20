import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.preprocessing import StandardScaler


class ChemSpace_PCA:
    def __init__(self, route, file_name):
        self.Data = pd.read_csv(f"{route}{file_name}")
        self.Data.head()
        print(self.Data.columns)
        print(self.Data.Library.unique())

    def pca_descriptors(self, feature_names):
        """
        output
            result: Data Frame with PCA result, 
            model: PCA Model
        """
        numerical_data = self.Data[feature_names]
        numerical_data = pd.DataFrame(StandardScaler().fit_transform(numerical_data))
        sklearn_pca = sklearn.decomposition.PCA(
            n_components=3, svd_solver="full", whiten=True
        )
        model = sklearn_pca.fit(numerical_data)
        loadings = model.components_
        loadings = np.transpose(loadings)
        PCA_loadings = pd.DataFrame(
            data = loadings, index=feature_names, columns=["PC 1", "PC 2", "PC 3"]
        )
        PCA_loadings.to_csv(
            "/Users/eurijuarez/Desktop/Alexis/pca_results/pca.csv"
        )
        pca_result = pd.DataFrame(
            model.transform(numerical_data), columns=["PC 1", "PC 2", "PC 3"]
        )
        _ = ["ID", "Library", "NEW_SMILES"]
        ref = self.Data[_]
        result = pd.concat([pca_result, ref], axis=1)
        variance = list(model.explained_variance_ratio_)
        cumulative_variance = np.cumsum(variance)
        summary = [variance, cumulative_variance]
        PCA_summary = pd.DataFrame(
            data=summary,
            index=["Percentage of variance", "Cummulative percentage of variance"],
            columns=["PC 1", "PC 2", "PC 3"],
        )
        PCA_summary.to_csv(
            "/Users/eurijuarez/Desktop/Alexis/pca_results/summary.csv"
        )
        a = round(variance[0] * 100, 2)
        b = round(variance[1] * 100, 2)

        # print(a,b)
        return result, a, b
