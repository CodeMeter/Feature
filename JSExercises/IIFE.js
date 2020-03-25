let sodiumChloride = (function(){
  let chemicalFormula = 'NaCl';
  let molarMass = 58.44;

  return {
    getProperties: function(){
      console.log(`Formula: ${chemicalFormula}`);
      console.log(`Molar Mass: ${molarMass} g/mol`);
    }
  };
})();

 sodiumChloride.getProperties();