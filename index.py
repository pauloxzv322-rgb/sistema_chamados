import streamlit as st

st.title("Sistema de Biblioteca")


#Criar lista de livros
if "livros" not in st.session_state:
    st.session_state.livros = []

#Cadastrar livro
st.subheader("Cadastrar Livro")
nome_livro = st.text_input("Nome do Livro")
autor_livro = st.text_input("Autor do Livro")

#Botão cadastrar
if st.button("Cadastrar livro"):
    
    if nome_livro != "" and autor_livro != "":
        livro = {
            "nome": nome_livro,
            "autor": autor_livro,
            "emprestado": False
        }

        st.session_state.livros.append(livro)
        st.success("Livro cadastrado com sucesso!")

#Listar livros
st.subheader("Livros Cadastrados")
if len(st.session_state.livros) == 0: 
    st.warning("Nenhum livro cadastrado.")
else:
    for i, livro in enumerate(st.session_state.livros):
        st.write(f"{livro['nome']}")
        st.write(f"Autor: {livro['autor']}")

        if livro["emprestado"] == False:
            st.success("Disponível")
        else:
            st.error("Emprestado")

        col1, col2 = st.columns(2)

 #Empréstimo
        with col1:
            if st.button("Emprestar", key=f"emprestado{i}"):
                    st.session_state.livros[i]["emprestado"] = True
                    st.rerun()
                
        with col2:
            if st.button("Devolver", key=f"devolver{i}"):
                    st.session_state.livros[i]["emprestado"] = False
                    st.rerun()
            st.divider()
                        