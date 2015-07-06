### Bridge Pattern

Il bridge pattern permette di separare l'astrazione di una classe dalla sua implementazione, per permettere loro di variare indipendentemente.

Per capire meglio pensiamo ad uno scenario reale, si vuole cambiare l’interfaccia grafica della nostra applicazione da Windows a Linux preservando la funzionalità di tutti i componenti grafici: in poche parole si vuole cambiare il LookAndFeel ma nello stesso momento fare in modo che il funzionamento rimanga inalterato.

Questo pattern è composto dai seguenti partecipanti:

-   Client(Main): colui che effettua l’invocazione all’operazione di interesse.
-   Abstraction(SistemaOperativo): definisce l’interfaccia del dominio applicativo utilizzata dal Client.
-   RefinedAbstraction(Testo): definisce l’implementazione dell’interfaccia utilizzata.
-   Implementor(SistemaOperativoAPI): definisce l’interfaccia da usare come Bridge e riferibile agli oggetti concreti da utilizzare.
-   ConcreteImplementor(Windows/Linux): implementa l’interfaccia Implementor usata come Bridge per il transito degli oggetti.


![Bridge UML](https://upload.wikimedia.org/wikipedia/commons/c/cf/Bridge_UML_class_diagram.svg)

Ora vediamone il codice:

