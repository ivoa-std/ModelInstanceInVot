[![PDF-Preview](https://img.shields.io/badge/PDF-Preview-blue)](https://github.com/ivoa-std/ModelInstanceInVot/releases/download/auto-pdf-preview/mivot-draft.pdf)
# Syntax proposal to map VOTable data on VO Model

This proposal is the merge of both annotations proposals that have been exercised durin the DM workshop held in 2021.

The objective is to provide a standard that allows to map VOTable data on any VO-DML compliant model. 

### Syntax Guide Lines

- Facilitate as much as possible the annotation of archival data
- Faith to the model structure
- As compact as possible

### Main Features

- The mapping is gathered in one block global for the VOTable
- The structure of the block is as follow
    - A reference to the mapped VODML
    - A set of globals instances that can be referenced by any other components
    - A Set of table mapping blocks: one per table 

### Resources

- `doc` : standard document
- `schema`: XML schema for the mapping syntax (XSD1.1)

### Document build up (from doc directory)

- Build the pdf: `make forcetex`
- Valid XML snippets: `make  valid_snippet`

# Licence

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
  <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
  <br />
  This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
  Creative Commons Attribution-ShareAlike 4.0 International License</a>.
  
