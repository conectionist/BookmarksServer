/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.bradvault.bookmarksserver.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Dan
 */
public class Database {

    protected Connection connection = null;
    protected static final Logger logger = Logger.getLogger(Database.class.getName());

    public Connection getConnection() {
        return connection;
    }
    
    public Database(String hostname, int port, String username, String password, String database) 
            throws SQLException, ClassNotFoundException
    {
        Class.forName("com.mysql.jdbc.Driver");
        
        String url = String.format("jdbc:mysql://%s:%d/%s?noAccessToProcedureBodies=true&useSSL=false", hostname, port, database);
        connection = DriverManager.getConnection(url, username, password);
    }
    
    @Override
    protected void finalize() throws Throwable {
        try {
            
            if (connection != null) {
                connection.close();
            }
        } catch (SQLException ex) {            
            logger.log(Level.WARNING, ex.getMessage(), ex);
        }
        
        super.finalize();
    }
}
