// Importa a função a ser testada (se estiver usando Node.js modules)
const validarEmail = require('./validarEmail'); 

// Bloco de testes para a funcionalidade
describe('Validação de E-mail', () => {

    // --- Implementação do seu Caso de Falha (TC-EMAIL-002) ---

    test('TC-EMAIL-002: Deve retornar FALSE para formato de e-mail inválido (sem @)', () => {
        const emailInvalido = "teste-email.com"; // Input sem o símbolo '@'
        
        // Assert: Espera-se que a função retorne False
        expect(validarEmail(emailInvalido)).toBe(false);
    });

    // --- Outros Casos de Falha para Robustez ---

    test.each([
        ['usuario@.com', 'Falta nome do domínio'],
        ['@dominio.com', 'Falta a parte local'],
        ['usuario@dominio', 'Falta TLD/extensão (.com, .net, etc.)'],
    ])('Deve rejeitar o e-mail inválido: %s', (email, descricao) => {
        expect(validarEmail(email)).toBe(false);
    });

    // --- Exemplo de Caso de Sucesso ---

    test('Deve retornar TRUE para um e-mail válido', () => {
        const emailValido = "contato.teste@empresa.com.br";
        expect(validarEmail(emailValido)).toBe(true);
    });

});