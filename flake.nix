{
    description = "A multi-threaded static HTTP server written in Rust";

    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    };

    outputs = { self, nixpkgs }: {
        devShells = builtins.mapAttrs (system: pkgs: {
            default = pkgs.mkShell {
                nativeBuildInputs = with pkgs; [
                    python314
                ];
            };
        }) nixpkgs.legacyPackages;
    };
}
