# spaltet eine Liste und gibt den Pivot zurück
def spalteListe(liste, von, bis):
    # Pivot ist das erste Element der zu spaltenden Liste
    pivot = liste[von]
    # die Grenze zwischen den kleinen und großen Werten ist am Anfang
    # der zu spaltenden Liste
    grenze = von

    # für jedes Element in der Liste
    for index in range(von+1, bis+1):
        # wenn das Element kleiner als der Pivot ist
        if liste[index] <= pivot:
            # die Grenze verschiebt sich eins nach rechts
            grenze+=1
            # tausche das Element mit dem Element an der Grenze
            liste[index], liste[grenze] = liste[grenze], liste[index]
        
    # vertausche die Grenze mit dem Pivot
    # Pivot ist jetzt zwischen den kleinen und großen Elementen
    liste[von], liste[grenze] = liste[grenze], liste[von]

    # gebe den Index des Pivots zurück
    return grenze

# sortiert eine Liste fertig
def quickSortSchritt(liste, von, bis):
    # wenn mindestens als ein Element sortiert werden muss
    if von < bis:
        # teile die Liste und speichere den pivot
        pivot = spalteListe(liste, von, bis)
        # sortiere die neuen Listen links und rechts von pivot
        quickSortSchritt(liste, von, pivot-1)
        quickSortSchritt(liste, pivot+1, bis)

    # gib die Liste zurück
    return liste

# sortiert eine Liste
def quickSort(liste):
    return quickSortSchritt(liste, 0, len(liste)-1)

liste = [1, 2, 3, 4, 5, 6, 7, 8]
quickSort(liste)
print(liste)
