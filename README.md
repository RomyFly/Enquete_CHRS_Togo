# Enquete_CHRS_Togo
Ce travail exercice virtuelle simullant une enquête de recherche au Centre Hospitalier Régional de Sokodé au Togo sur les Facteurs socioculturels associés à la décompensation de l’hypertension artérielle ciblant des patients âgés d’au moins 18 ans et atteint d'hypertension arterielle.

Dans le cadre d’une recherche qui va être mené au Centre Hospitalier Régional de Sokodé au Togo sur les Facteurs socioculturels associés à la décompensation de l’hypertension artérielle qui cible 84 patients âgés d’au moins 18 ans dont 42 présentent une hypertension compensée et 42 présentent une hypertension décompensée.Il a été demandé à notre équipe de fournir des outils afin de permettre la collecte et l’analyse des données.
1-	Elaboration de l’outil de collecte
- Le formulaire de collecte devra être développé sur Streamlit et permettre les enregistrements doivent se faire dans une base de données SQLite ou un fichier Microsoft Excel.
Les variables d’intérêt sont présentées dans le tableau ci-dessous :


+----------------------------------------------+---------------------------+-----------------------+--------------------------+
+               Facteurs                       +      Variables            +         Type          +         Modalités        +
+----------------------------------------------+---------------------------+-----------------------+--------------------------+
+                                              +                           +                       +         Compensée        +
+               Pathologie                     +  Hypertension arterielle  +        Nominale       +--------------------------+
+                                              +                           +                       +        Décompensée       +
+----------------------------------------------+---------------------------+-----------------------+--------------------------+
+                                              +                           +                       +         Masculin         +
+                                              +            Sexe           +        Nominale       +--------------------------+
+                                              +                           +                       +         Feminin          +
+                                              +---------------------------+-----------------------+--------------------------+
+                                              +         Date de           +         Date          + À partir du 21-07-2006   +
+                                              +        Naissance          +                       + au format « DD-MM-YYYY » +
+     Facteurs sociodémographiques             +---------------------------+-----------------------+--------------------------+
+                                              +                           +                       +     Non alphabétisé      +
+                                              +                           +                       +--------------------------+
+                                              +                           +                       +         Primaire         +
+                                              +      Niveau d’étude       +        Nominale       +--------------------------+
+                                              +                           +                       +        Secondaire        +
+                                              +                           +                       +--------------------------+
+                                              +                           +                       +       Universitaire      +
+----------------------------------------------+---------------------------+-----------------------+--------------------------+
+                                              +                           +                       +    Profession physique   +
+                                              +     Type de profession    +        Nominale       +--------------------------+
+                                              +                           +                       +  Profession non-physique +
+                                              +---------------------------+-----------------------+--------------------------+
+                                              +    Activité Sportive en   +       Discrète        + Nombre d’heure d'exercice+
+                                              + nombre d’heure par semaine+                       +        par semaine       +
+                                              +---------------------------+-----------------------+--------------------------+
+                                              +                           +                       +            Oui           +
+                                              +         Solitude          + 	  Dichotomique     +--------------------------+
+                                              +                           +                       +            Non           +
+                                              +---------------------------+-----------------------+--------------------------+
+                                              +                           +                       +            Oui           +
+        Facteurs socioculturels               +   Relation conflictuelle  + 	  Dichotomique     +--------------------------+
+                                              +                           +                       +            Non           +
+                                              +---------------------------+-----------------------+--------------------------+
+                                              + Méconnaissance des        +                       +            Oui           +
+                                              + Facteurs de risque de     + 	  Dichotomique     +--------------------------+
+                                              + l'HTA                     +                       +            Non           +
+                                              +---------------------------+-----------------------+--------------------------+
+                                              + Manque de soutien social  +                       +            Oui           +
+                                              + et Economique             + 	  Dichotomique     +--------------------------+
+                                              +                           +                       +            Non           +
+----------------------------------------------+---------------------------+-----------------------+--------------------------+


-	Prévoir pour l’outil que les données puissent être saisie manuellement afin d’alimenter la base de données
-	Mais aussi que les données puissent être chargées grâce à un fichier Excel

