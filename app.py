import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_sales(data):
    # Calculer les ventes totales par mois
    monthly_sales = data.groupby('Month')['Sales'].sum()

    # Trouver le produit le plus vendu
    top_product = data.groupby('Product')['Sales'].sum().idxmax()

    # Retourner les statistiques
    return monthly_sales, top_product

def generate_plots(monthly_sales):
    # Générer un graphique des ventes mensuelles
    plt.figure(figsize=(10, 6))
    monthly_sales.plot(kind='bar')
    plt.title('Ventes Mensuelles')
    plt.xlabel('Mois')
    plt.ylabel('Ventes en USD')
    plt.savefig('output/monthly_sales.png')

def export_report(monthly_sales, top_product):
    # Créer un dossier de sortie si nécessaire
    if not os.path.exists('output'):
        os.makedirs('output')

    # Exporter les statistiques dans un fichier texte
    with open('output/report.txt', 'w') as f:
        f.write("Rapport d'Analyse des Ventes\n")
        f.write("===========================\n\n")
        f.write("Ventes Mensuelles:\n")
        f.write(monthly_sales.to_string())
        f.write("\n\nProduit le plus vendu:\n")
        f.write(f"{top_product}\n")

if __name__ == "__main__":
    # Charger les données depuis le fichier CSV
    data = pd.read_csv('sales_data.csv')

    # Analyser les données
    monthly_sales, top_product = analyze_sales(data)

    # Générer les graphiques
    generate_plots(monthly_sales)

    # Exporter le rapport
    export_report(monthly_sales, top_product)

    print("Analyse terminée. Rapport généré dans le dossier 'output'.")
