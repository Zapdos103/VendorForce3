
/* Funcoes do painel */

function redirecionarParaCandidatos() {
        window.location.href = "/painel/candidatos_empresa/";
    }

function redirecionarParaConfig() {
        window.location.href = "/painel/config_empresa/";
    }

function redirecionarParaRelatorio() {
        window.location.href = "/painel/relatorios_empresa/";
    }

function redirecionarParaDashboard() {
        window.location.href = "/painel/dashboard_empresa";
}

function redirecionarParaFuncionario() {
        window.location.href = "/auth/cadastro_funcionario";
}

function logoutEmpresa() {
        if (confirm('Deseja mesmo sair da conta?')) {
            window.location.href = "/auth/logout_empresa/";
        }

}
