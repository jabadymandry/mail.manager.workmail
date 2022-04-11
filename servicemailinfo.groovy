// Static content examples. These lists can be generated dynamically as an alternative.
// OrganisationId, DomainName, SenderEmailAddress, SmtpPassCredential

List ProdigyMail  = ["Select:selected", "m-c5593a91faa84f8cad7721c01b0f4b90", "prodigy.gov.mg", "bruno@prodigy.gov.mg", "0dbee823-44c5-4e66-8297-92e3fd3c53da"]
List DigitalMail  = ["Select:selected", "m-35959561b27a4d4b8408a9fe2f5daba4", "digital.gov.mg", "mailman@prodigy.gov.mg", "0dbee823-44c5-4e66-8297-92e3fd3c53da"]
List MndptMail  = ["Select:selected", "m-deff13a8a7ff436dbc7ad38a690f861e", "mndpt.gov.mg", "mailman@prodigy.gov.mg", "0dbee823-44c5-4e66-8297-92e3fd3c53da"]
List CirtMail  = ["Select:selected", "m-40067b6aa0cc44a6b8bad1b8a7a50985", "cirt.gov.mg", "mailman@prodigy.gov.mg", "0dbee823-44c5-4e66-8297-92e3fd3c53da"]

List default_item = ["None"]

if (DomainName == 'PRODIGY.GOV.MG') {
  return ProdigyMail
} else if (DomainName == 'DIGITAL.GOV.MG') {
  return DigitalMail
} else if (DomainName == 'MNDPT.GOV.MG') {
  return MndptMail
} else if (DomainName == 'CIRT.GOV.MG') {
  return CirtMail
} else {
  return default_item
}